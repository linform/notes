# Install a per-user Windows task; no password or administrator run level.
param(
    [string]$RepositoryPath = $PSScriptRoot,
    [switch]$Describe,
    [switch]$Uninstall
)

$ErrorActionPreference = 'Stop'
try {
    $commonDirectory = & git -C $RepositoryPath rev-parse --path-format=absolute --git-common-dir
    if ($LASTEXITCODE -ne 0) { throw 'Repository is unavailable.' }
    $normalized = [IO.Path]::GetFullPath($commonDirectory).TrimEnd('\', '/').ToLowerInvariant()
    $hasher = [Security.Cryptography.SHA256]::Create()
    try { $hash = [BitConverter]::ToString($hasher.ComputeHash([Text.Encoding]::UTF8.GetBytes($normalized))).Replace('-', '').Substring(0, 12).ToLowerInvariant() }
    finally { $hasher.Dispose() }
    $taskName = "NotesAutoSync-$hash"

    $mainDirectory = $null
    $candidate = $null
    $worktrees = @(& git -C $RepositoryPath -c core.quotepath=false worktree list --porcelain)
    if ($LASTEXITCODE -ne 0) { throw 'Cannot inspect repository worktrees.' }
    foreach ($line in $worktrees) {
        if ($line.StartsWith('worktree ')) { $candidate = $line.Substring(9) }
        elseif ($line -eq 'branch refs/heads/main') { $mainDirectory = $candidate }
    }
    if (-not $mainDirectory) { throw 'No working directory on main. Check out main before installing auto sync.' }
    $workerPath = Join-Path $mainDirectory 'auto-sync.ps1'
    if (-not (Test-Path -LiteralPath $workerPath)) { throw 'The main directory does not contain auto-sync.ps1.' }
    $description = "Notes auto sync for $mainDirectory"

    if ($Uninstall -and -not $Describe) {
        $existing = Get-ScheduledTask -TaskName $taskName -TaskPath '\' -ErrorAction SilentlyContinue
        if ($existing) {
            if ($existing.Description -ne $description) { throw 'Task name belongs to another configuration; refusing to change it.' }
            Stop-ScheduledTask -TaskName $taskName -TaskPath '\'
            Unregister-ScheduledTask -TaskName $taskName -TaskPath '\' -Confirm:$false
        }
        Write-Host "[Auto Start] Removed $taskName."
        exit 0
    }

    $userSid = [Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    $powershellPath = Join-Path $env:WINDIR 'System32\WindowsPowerShell\v1.0\powershell.exe'
    $logPath = Join-Path $mainDirectory 'site\auto-sync-task.log'
    $arguments = '-NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File "' + $workerPath + '" -LogPath "' + $logPath + '" -Unattended'
    $action = New-ScheduledTaskAction -Execute $powershellPath -Argument $arguments -WorkingDirectory $mainDirectory
    $principal = New-ScheduledTaskPrincipal -UserId $userSid -LogonType Interactive -RunLevel Limited
    $login = New-ScheduledTaskTrigger -AtLogOn -User $userSid
    # With no repetition duration, retry continues indefinitely. IgnoreNew
    # prevents the recovery trigger from launching a second running instance.
    $recovery = New-ScheduledTaskTrigger -Once -At ((Get-Date).AddMinutes(5)) -RepetitionInterval (New-TimeSpan -Minutes 5)
    $settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -ExecutionTimeLimit ([TimeSpan]::Zero) -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1) -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
    $definition = New-ScheduledTask -Action $action -Trigger @($login, $recovery) -Settings $settings -Principal $principal -Description $description

    if ($Describe) {
        # Inspect the actual task objects without registering or starting them.
        [pscustomobject]@{
            TaskName = $taskName
            MainDirectory = $mainDirectory
            Action = $action | Select-Object Execute, Arguments, WorkingDirectory
            Principal = $principal | Select-Object UserId, LogonType, RunLevel
            Settings = $settings | Select-Object MultipleInstances, ExecutionTimeLimit, RestartCount, RestartInterval, StartWhenAvailable, DisallowStartIfOnBatteries, StopIfGoingOnBatteries
            Triggers = @($login, $recovery) | ForEach-Object {
                [pscustomobject]@{ Kind = $_.CimClass.CimClassName; UserId = $_.UserId; Interval = $_.Repetition.Interval; Duration = $_.Repetition.Duration }
            }
        } | ConvertTo-Json -Depth 5
        exit 0
    }

    $existing = Get-ScheduledTask -TaskName $taskName -TaskPath '\' -ErrorAction SilentlyContinue
    if ($existing -and $existing.Description -ne $description) {
        throw 'Task name belongs to another configuration; refusing to change it.'
    }
    if ($existing -and $existing.State -eq 'Running') {
        Stop-ScheduledTask -TaskName $taskName -TaskPath '\'
    }
    $null = Register-ScheduledTask -TaskName $taskName -TaskPath '\' -InputObject $definition -Force
    Start-ScheduledTask -TaskName $taskName -TaskPath '\'
    Write-Host "[Auto Start] Installed and started $taskName."
    Write-Host "[Auto Start] Main directory: $mainDirectory"
    Write-Host "[Auto Start] Log: $logPath"
}
catch {
    Write-Warning "[Auto Start] $($_.Exception.Message)"
    exit 1
}
