param(
    [Parameter(Mandatory=$true)]
    [string]$Name,
    [string]$Deck = "*"
)

$searchPath = Join-Path $PSScriptRoot "..\printables\*$Deck*.html"
$matches = Select-String -Path $searchPath -Pattern $Name -Context 2, 12

if (-not $matches) {
    Write-Host "No card matching '$Name' found in $searchPath."
    exit 0
}

foreach ($m in $matches) {
    Write-Host "=== Found in $($m.Path | Split-Path -Leaf) (Line $($m.LineNumber)) ===" -ForegroundColor Cyan
    $m.Context.PreContext | ForEach-Object { Write-Host "  $_" }
    Write-Host "> $($m.Line)" -ForegroundColor Yellow
    $m.Context.PostContext | ForEach-Object { Write-Host "  $_" }
    Write-Host ""
}

