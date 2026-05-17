$VENV_PATH = "D:\\person\\git\\\venv-p13\\Scripts\\Activate.ps1"
$SCRIPT1 = "D:\\person\\git\\soundboard\\keyboard-listener.py"
$SCRIPT2 = "D:\\person\\git\\soundboard\\audio-player.py"

$JobBlock1 = [scriptblock]::Create(". '$VENV_PATH'; python '$SCRIPT1'")
$JobBlock2 = [scriptblock]::Create(". '$VENV_PATH'; python '$SCRIPT2'")

Write-Host "Starting soundboard scripts as background jobs"

$Job1 = Start-Job -ScriptBlock $JobBlock1
Start-Sleep -Seconds 2
$Job2 = Start-Job -ScriptBlock $JobBlock2

Read-Host -Prompt "Press enter to stop soundboard"

Remove-Job -Job @($Job1, $Job2) -Force

Write-Host "`n--- Output from $SCRIPT1 ---"
Receive-Job -Job $Job1

Write-Host "`n--- Output from $SCRIPT2 ---"
Receive-Job -Job $Job2

Read-Host -Prompt "Press enter to close"
