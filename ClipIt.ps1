# === ClipIT.ps1 ===

# Configurable paths
$pythonPath = "Path\to\python" # Full path to python.exe
$scriptPath = "Path\to\main.pyw (absolute)"        # Full path to the Python script
$pidPath = "Path\to\pid.text (absolute)"  # File to write the PID to

# Launch Python script as a new process
$proc = Start-Process -FilePath $pythonPath `
                     -ArgumentList "`"$scriptPath`"" `
                     -PassThru

# Write its PID to a file for OBS to read
$proc.Id | Out-File -FilePath $pidPath -Encoding ascii

Write-Host "Launched Python script with PID $($proc.Id)"
