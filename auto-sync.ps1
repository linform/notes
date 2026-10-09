# Automatically commits docs/ and mkdocs.yml and pushes the main branch.
# Runs only while VS Code is open. No force-push or automatic merges.
$ErrorActionPreference = 'Continue'
Set-Location -LiteralPath $PSScriptRoot

Write-Host '[Auto Sync] Started. Checking for changes every 60 seconds.'
Write-Host '[Auto Sync] Watching: docs/, mkdocs.yml'
Write-Host '[Auto Sync] Press Ctrl+C to stop.'

while ($true) {
    Start-Sleep -Seconds 60

    $changes = @(git status --porcelain -- docs mkdocs.yml)
    if ($LASTEXITCODE -ne 0) {
        Write-Warning '[Auto Sync] git status failed. Retrying later.'
        continue
    }

    if (-not [string]::IsNullOrWhiteSpace(($changes -join ''))) {
        git add -A -- docs mkdocs.yml
        if ($LASTEXITCODE -ne 0) {
            Write-Warning '[Auto Sync] git add failed. Retrying later.'
            continue
        }

        git diff --cached --quiet -- docs mkdocs.yml
        if ($LASTEXITCODE -eq 1) {
            $message = 'Auto sync notes ' + (Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
            git commit -m $message -- docs mkdocs.yml
            if ($LASTEXITCODE -ne 0) {
                Write-Warning '[Auto Sync] Commit failed. Retrying later.'
                continue
            }
        }
        elseif ($LASTEXITCODE -ne 0) {
            Write-Warning '[Auto Sync] Cannot inspect staged changes.'
            continue
        }
    }

    # Retry pending pushes after temporary network outages.
    $pending = git rev-list --count origin/main..HEAD 2>$null
    if ($LASTEXITCODE -eq 0 -and [int]$pending -gt 0) {
        git push origin main
        if ($LASTEXITCODE -eq 0) {
            Write-Host '[Auto Sync] GitHub updated successfully.'
        }
        else {
            Write-Warning '[Auto Sync] Push failed. Check your network, credentials or remote changes.'
            Write-Warning '[Auto Sync] Remote conflicts must be resolved manually. Never force-push.'
        }
    }
}
