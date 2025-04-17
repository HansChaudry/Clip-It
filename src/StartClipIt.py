import obspython as obs
import subprocess
import os
import signal
import time

ps_proc = None
child_pid = None

def script_load(settings):
    global ps_proc, child_pid

    current_dir = os.path.dirname(os.path.abspath(__file__))
    ps1_script = os.path.join(current_dir, "ClipIt.ps1")
    pid_file = os.path.join(current_dir, "pid.txt")

    # Start the PowerShell script
    try:
        ps_proc = subprocess.Popen([
            "powershell.exe",
            "-ExecutionPolicy", "Bypass",
            "-File", ps1_script
        ])
        print("PowerShell launcher script started.")
    except Exception as e:
        print("Failed to launch PowerShell script:", e)
        return

    # Wait up to 5 seconds for PID file to appear
    timeout = 5
    while timeout > 0:
        if os.path.exists(pid_file):
            try:
                with open(pid_file, "r") as f:
                    pid = f.read().strip()
                    if pid.isdigit():
                        child_pid = int(pid)
                        print(f"Found child Python script PID: {child_pid}")
                        break
            except Exception as e:
                print("Error reading PID file:", e)
        time.sleep(1)
        timeout -= 1

def script_unload():
    global ps_proc, child_pid

    print("OBS is unloading script. Cleaning up...")

    # Check if PowerShell process is running
    if ps_proc:
        try:
            if ps_proc.poll() is None:  # Process is still running
                ps_proc.terminate()
                ps_proc.wait(timeout=3)
                print("PowerShell process terminated.")
            else:
                print("PowerShell process already terminated.")
        except Exception as e:
            print("Error terminating PowerShell process:", e)

    # Check if child Python process is still running
    if child_pid:
        try:
            os.kill(child_pid, signal.SIGTERM)
            print(f"Terminated Python script with PID {child_pid}")
        except Exception as e:
            print(f"Failed to terminate child process {child_pid}: {e}")

    # Clean up PID file
    pid_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pid.txt")
    if os.path.exists(pid_file):
        try:
            with open(pid_file, "w") as f:
                f.truncate(0)  # Empty the PID file
            print("Cleared PID file.")
        except Exception as e:
            print(f"Error clearing PID file: {e}")
