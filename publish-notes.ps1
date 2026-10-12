# Explicit completion-time publishing, including linked and detached worktrees.
param(
    [string]$PythonPath,
    [string]$Message = 'Publish completed study notes',
    [switch]$IncludeCommittedProjectChanges
)

$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

function Read-Git {
    param([string]$Directory, [string[]]$Arguments)
    # Avoid PowerShell 5.1 treating normal native stderr as a terminating error.
    $savedPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $output = @(& git -C $Directory @Arguments 2>&1)
        if ($LASTEXITCODE -ne 0) {
            throw "Git failed: git $($Arguments -join ' ')`n$($output -join "`n")"
        }
        return ($output | ForEach-Object { $_.ToString() })
    }
    finally { $ErrorActionPreference = $savedPreference }
}

function Test-Ancestor {
    param([string]$Older, [string]$Newer)
    & git merge-base --is-ancestor $Older $Newer
    if ($LASTEXITCODE -gt 1) { throw 'Cannot inspect commit ancestry.' }
    return $LASTEXITCODE -eq 0
}

function Assert-Idle {
    param([string]$Directory)
    foreach ($marker in @('MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'rebase-merge', 'rebase-apply')) {
        $markerPath = Read-Git $Directory @('rev-parse', '--path-format=absolute', '--git-path', $marker)
        if (Test-Path -LiteralPath $markerPath) { throw "Git operation is in progress in $Directory." }
    }
    if (@(Read-Git $Directory @('ls-files', '--unmerged')).Count -gt 0) {
        throw "Unresolved conflicts in $Directory."
    }
}

function Assert-OnlyNotes {
    param([string[]]$Paths)
    foreach ($path in $Paths) {
        if ($path -ne 'mkdocs.yml' -and -not $path.StartsWith('docs/')) {
            throw "Unreviewed project changes: $path. Commit reviewed task files explicitly, then use -IncludeCommittedProjectChanges."
        }
    }
}

$operationMutex = $null
$ownsOperation = $false
try {
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Git is unavailable.' }
    $source = (Read-Git $PSScriptRoot @('rev-parse', '--show-toplevel')).Trim()
    $commonDirectory = (Read-Git $source @('rev-parse', '--path-format=absolute', '--git-common-dir')).Trim()
    $normalized = [IO.Path]::GetFullPath($commonDirectory).TrimEnd('\', '/').ToLowerInvariant()
    $hasher = [Security.Cryptography.SHA256]::Create()
    try { $lockHash = [BitConverter]::ToString($hasher.ComputeHash([Text.Encoding]::UTF8.GetBytes($normalized))).Replace('-', '') }
    finally { $hasher.Dispose() }

    # The background worker has a separate lifetime lock; publishing only takes
    # the shared operation lock, so an idle worker need not be stopped.
    $operationMutex = [Threading.Mutex]::new($false, "Local\NotesSyncOperation-$lockHash")
    try { $ownsOperation = $operationMutex.WaitOne(30000) }
    catch [Threading.AbandonedMutexException] { $ownsOperation = $true }
    if (-not $ownsOperation) { throw 'Another sync operation is running. Retry after it finishes.' }

    $mainDirectory = $null
    $candidate = $null
    foreach ($line in (Read-Git $source @('-c', 'core.quotepath=false', 'worktree', 'list', '--porcelain'))) {
        if ($line.StartsWith('worktree ')) { $candidate = $line.Substring(9) }
        elseif ($line -eq 'branch refs/heads/main') { $mainDirectory = $candidate }
    }
    if (-not $mainDirectory) { throw 'No worktree on main. Check out main in the main working directory before publishing.' }
    Assert-Idle $source
    Assert-Idle $mainDirectory
    $sameDirectory = [IO.Path]::GetFullPath($source).TrimEnd('\', '/') -eq [IO.Path]::GetFullPath($mainDirectory).TrimEnd('\', '/')
    if (-not $sameDirectory) {
        $dirty = @(Read-Git $mainDirectory @('status', '--porcelain', '--untracked-files=no'))
        if ($dirty.Count -gt 0) { throw 'Main working directory has uncommitted changes. Preserve and reconcile them before publishing.' }
    }

    $workingChanges = @(Read-Git $source @('-c', 'core.quotepath=false', 'diff', 'HEAD', '--name-only'))
    Assert-OnlyNotes $workingChanges
    $null = Read-Git $source @('fetch', '--quiet', '--no-tags', 'origin', 'refs/heads/main')
    $remote = (Read-Git $source @('rev-parse', 'FETCH_HEAD')).Trim()
    $main = (Read-Git $source @('rev-parse', 'refs/heads/main')).Trim()
    $head = (Read-Git $source @('rev-parse', 'HEAD')).Trim()
    if (-not (Test-Ancestor $main $head)) { throw 'Main has changes not included in this worktree. Reconcile before publishing.' }
    if (-not (Test-Ancestor $remote $head)) { throw 'Remote main has changes not included in this worktree. Reconcile before publishing.' }
    if (-not $IncludeCommittedProjectChanges) {
        # Inspect every pending commit, not just the final net diff.
        $pending = @(Read-Git $source @('-c', 'core.quotepath=false', 'log', '--format=', '--name-only', "$remote..$head"))
        Assert-OnlyNotes @($pending | Where-Object { $_ -ne '' })
    }

    if (-not $PythonPath) {
        foreach ($directory in @($source, $mainDirectory)) {
            $pythonCandidate = Join-Path $directory '.venv\Scripts\python.exe'
            if (Test-Path -LiteralPath $pythonCandidate) { $PythonPath = $pythonCandidate; break }
        }
    }
    if (-not $PythonPath) { throw 'Python environment missing. Set up .venv or pass -PythonPath.' }
    if (-not (Get-Command $PythonPath -ErrorAction SilentlyContinue)) { throw 'The selected Python command is unavailable.' }
    $savedPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        & $PythonPath -m mkdocs build --strict --site-dir (Join-Path $source 'site\publish-preview')
        $buildExit = $LASTEXITCODE
    }
    finally { $ErrorActionPreference = $savedPreference }
    if ($buildExit -ne 0) { throw 'Strict documentation build failed. Nothing was published.' }
    if ((Read-Git $source @('rev-parse', 'HEAD')).Trim() -ne $head) {
        throw 'Worktree HEAD changed during validation. Reconcile before publishing.'
    }
    Assert-Idle $source

    # A single commit can update main itself when invoked there. Only the notes
    # paths are staged and committed; untracked files elsewhere stay local.
    $changes = @(Read-Git $source @('status', '--porcelain', '--', 'docs', 'mkdocs.yml'))
    if ($changes.Count -gt 0) {
        $null = Read-Git $source @('add', '-A', '--', 'docs', 'mkdocs.yml')
        $null = Read-Git $source @('diff', '--cached', '--check', '--', 'docs', 'mkdocs.yml')
        $commitOutput = Read-Git $source @('commit', '-m', $Message, '--', 'docs', 'mkdocs.yml')
        $commitOutput | ForEach-Object { Write-Host $_ }
    }
    $target = (Read-Git $source @('rev-parse', 'HEAD')).Trim()
    # Recheck both directories after the build; an editor may have changed main.
    Assert-Idle $source
    Assert-Idle $mainDirectory
    if ((Read-Git $mainDirectory @('symbolic-ref', '--quiet', 'HEAD')).Trim() -ne 'refs/heads/main') {
        throw 'Main directory changed branches during validation. Local commit retained.'
    }
    if (-not $sameDirectory -and (Read-Git $mainDirectory @('rev-parse', 'HEAD')).Trim() -ne $main) {
        throw 'Main HEAD changed during validation. Local commit retained; reconcile before retrying.'
    }
    if (-not $sameDirectory -and @(Read-Git $mainDirectory @('status', '--porcelain', '--untracked-files=no')).Count -gt 0) {
        throw 'Main changed during validation. Local commit retained; reconcile before retrying.'
    }
    $mergeOutput = Read-Git $mainDirectory @('merge', '--ff-only', $target)
    $mergeOutput | ForEach-Object { Write-Host $_ }
    if ((Read-Git $mainDirectory @('rev-parse', 'HEAD')).Trim() -ne $target) {
        throw 'Main is not at the validated target. Nothing was pushed.'
    }
    $pushOutput = Read-Git $mainDirectory @('push', 'origin', "${target}:refs/heads/main")
    $pushOutput | ForEach-Object { Write-Host $_ }
    $verified = @(Read-Git $source @('ls-remote', '--exit-code', 'origin', 'refs/heads/main'))
    if ($verified.Count -ne 1 -or ($verified[0] -split '\s+')[0] -ne $target) {
        throw 'Remote verification failed. Do not report this task as synchronized.'
    }
    Write-Host "[Publish] Pushed and verified main at $target."
    Write-Host '[Publish] Now check the GitHub Actions run for this SHA; website deployment is a separate completion condition.'
    exit 0
}
catch {
    Write-Warning "[Publish] $($_.Exception.Message)"
    Write-Warning '[Publish] Incomplete. Existing commits and files are retained; fix the reported condition and retry.'
    exit 1
}
finally {
    if ($ownsOperation) { $operationMutex.ReleaseMutex() }
    if ($operationMutex) { $operationMutex.Dispose() }
}
