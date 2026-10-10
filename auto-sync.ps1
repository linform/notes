# Automatically commits docs/ and mkdocs.yml on main only.
# No automatic pull, merge, rebase, or force-push.
param(
    [ValidateRange(1, 86400)]
    [int]$IntervalSeconds = 60,
    [switch]$Once
)

$ErrorActionPreference = 'Continue'
Set-Location -LiteralPath $PSScriptRoot

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Warning '[Auto Sync] Git is unavailable. Install Git and restart VS Code.'
    exit 1
}

function Test-SyncState {
    $branch = git symbolic-ref --quiet HEAD 2>$null
    if ($LASTEXITCODE -ne 0 -or $branch -ne 'refs/heads/main') {
        Write-Warning '[Auto Sync] Sync requires the main branch. Detached HEAD and other branches are skipped without staging or committing.'
        return $false
    }

    foreach ($marker in @('MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'rebase-merge', 'rebase-apply')) {
        $markerPath = git rev-parse --git-path $marker
        if ($LASTEXITCODE -ne 0) { return $false }
        if (Test-Path -LiteralPath $markerPath) {
            Write-Warning '[Auto Sync] A Git operation is in progress. Finish or abort it manually before syncing.'
            return $false
        }
    }

    $unmerged = @(git ls-files --unmerged)
    if ($LASTEXITCODE -ne 0 -or $unmerged.Count -gt 0) {
        Write-Warning '[Auto Sync] Cannot sync with unresolved conflicts.'
        return $false
    }
    return $true
}

function Invoke-NotesSync {
    if (-not (Test-SyncState)) { return $false }

    $changes = @(git status --porcelain -- docs mkdocs.yml)
    if ($LASTEXITCODE -ne 0) {
        Write-Warning '[Auto Sync] Cannot inspect notes. Retrying later.'
        return $false
    }

    if (-not [string]::IsNullOrWhiteSpace(($changes -join ''))) {
        git add -A -- docs mkdocs.yml | Out-Host
        if ($LASTEXITCODE -ne 0) {
            Write-Warning '[Auto Sync] Cannot stage notes. Retrying later.'
            return $false
        }

        git diff --cached --quiet -- docs mkdocs.yml
        $diffExit = $LASTEXITCODE
        if ($diffExit -eq 1) {
            if (-not (Test-SyncState)) { return $false }
            $message = 'Auto sync notes ' + (Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
            git commit -m $message -- docs mkdocs.yml | Out-Host
            if ($LASTEXITCODE -ne 0) {
                Write-Warning '[Auto Sync] Commit failed. Retrying later.'
                return $false
            }
            Write-Host '[Auto Sync] Notes committed locally.'
        }
        elseif ($diffExit -ne 0) {
            Write-Warning '[Auto Sync] Cannot inspect staged notes.'
            return $false
        }
    }

    # Fetch the target explicitly; do not rely on a stale origin/main.
    # Windows PowerShell wraps native stderr in ErrorRecord, even for Git progress.
    # Print its text without a misleading exception banner; still check the exit code.
    git fetch --quiet --no-tags origin refs/heads/main 2>&1 | ForEach-Object { $_.ToString() } | Out-Host
    if ($LASTEXITCODE -ne 0) {
        Write-Warning '[Auto Sync] Cannot read remote main. Local commits are retained; retrying later.'
        return $false
    }
    $remoteCommit = git rev-parse FETCH_HEAD
    if ($LASTEXITCODE -ne 0) { return $false }
    $localCommit = git rev-parse refs/heads/main
    if ($LASTEXITCODE -ne 0) { return $false }

    if ($remoteCommit -eq $localCommit) {
        Write-Host '[Auto Sync] No pending commits on main.'
        return $true
    }

    git merge-base --is-ancestor $remoteCommit $localCommit
    if ($LASTEXITCODE -ne 0) {
        Write-Warning '[Auto Sync] Remote main has changes not included locally. Reconcile them manually; no automatic merge or force-push was attempted.'
        return $false
    }
    if (-not (Test-SyncState)) { return $false }

    # Push the exact commit we inspected, then verify the remote branch.
    git push origin "${localCommit}:refs/heads/main" 2>&1 | ForEach-Object { $_.ToString() } | Out-Host
    if ($LASTEXITCODE -ne 0) {
        Write-Warning '[Auto Sync] Push failed. Local commits are retained; check network, credentials, or remote changes.'
        return $false
    }
    $remoteRef = @(git ls-remote --exit-code origin refs/heads/main)
    if ($LASTEXITCODE -ne 0 -or $remoteRef.Count -ne 1) {
        Write-Warning '[Auto Sync] Push returned successfully, but remote verification failed. Retrying later.'
        return $false
    }
    $verifiedCommit = ($remoteRef[0] -split '\s+')[0]
    if ($verifiedCommit -ne $localCommit) {
        Write-Warning '[Auto Sync] Remote main changed during verification. Check its history before continuing.'
        return $false
    }

    Write-Host "[Auto Sync] Pushed and verified main at $localCommit."
    Write-Host '[Auto Sync] Website deployment is separate. Check https://github.com/linform/notes/actions'
    return $true
}

if (-not (Test-SyncState)) { exit 1 }

# Share a lock across processes and linked worktrees in this Windows session.
# A named mutex is released by Windows even if the worker is forcibly stopped.
$gitDirectory = git rev-parse --path-format=absolute --git-common-dir
if ($LASTEXITCODE -ne 0) { exit 1 }
$repositoryPath = [IO.Path]::GetFullPath($gitDirectory).TrimEnd('\', '/').ToLowerInvariant()
$hasher = [Security.Cryptography.SHA256]::Create()
try {
    $lockHash = [BitConverter]::ToString($hasher.ComputeHash([Text.Encoding]::UTF8.GetBytes($repositoryPath))).Replace('-', '')
}
finally { $hasher.Dispose() }
$syncMutex = [Threading.Mutex]::new($false, "Local\NotesAutoSync-$lockHash")
$ownsLock = $false
try {
    try { $ownsLock = $syncMutex.WaitOne(0) }
    catch [Threading.AbandonedMutexException] { $ownsLock = $true }
    if (-not $ownsLock) {
        Write-Warning '[Auto Sync] Another sync worker is already running for this repository. Stop it before starting a new worker or using -Once.'
        exit 1
    }

    if ($Once) {
        if (Invoke-NotesSync) { exit 0 }
        exit 1
    }

    Write-Host "[Auto Sync] Checking docs/ and mkdocs.yml every $IntervalSeconds seconds on main."
    Write-Host '[Auto Sync] Other files require manual commits. Press Ctrl+C to stop.'
    while ($true) {
        Start-Sleep -Seconds $IntervalSeconds
        $null = Invoke-NotesSync
    }
}
finally {
    if ($ownsLock) { $syncMutex.ReleaseMutex() }
    $syncMutex.Dispose()
}
