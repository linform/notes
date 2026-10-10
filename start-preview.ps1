# Start the preview using this checkout's virtual environment.
param(
    [string]$Address = '127.0.0.1:8000'
)

$ErrorActionPreference = 'Continue'
Set-Location -LiteralPath $PSScriptRoot
$pythonPath = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'

if (-not (Test-Path -LiteralPath $pythonPath)) {
    Write-Host '[Preview] The local Python environment is missing. Run these commands in this folder:'
    Write-Host '  py -3.12 -m venv .venv'
    Write-Host '  .\.venv\Scripts\python.exe -m pip install -r requirements.txt'
    Write-Host '[Preview] See README.md for setup and troubleshooting.'
    exit 1
}

& $pythonPath -c 'import mkdocs, material, pymdownx' 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host '[Preview] Dependencies are missing. Run:'
    Write-Host '  .\.venv\Scripts\python.exe -m pip install -r requirements.txt'
    exit 1
}

& $pythonPath -m mkdocs serve --dev-addr $Address
exit $LASTEXITCODE
