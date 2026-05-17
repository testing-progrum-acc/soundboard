# soundboard
play a random sound on key input


## Setup
Python version 13 or lower is currently a requirement on Windows, as pydub currently won't install on 14 or greater.

Set the AUDIO_DIR variable in audio-player.py

VENV_PATH,SCRIPT1, and SCRIPT2 in simple-runner.ps1

### Optional
To run on login, in shell:startup create a shortcut to:
```C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File "D:\person\git\soundboard\simple-runner.ps1"```