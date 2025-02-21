import psutil
import time

def check_process(process_name):
    """Check whether the specified process is started"""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False

# Set the target process name for detection
target_process = "Notepad.exe"

while True:
    if check_process(target_process):
        print(f"Detected '{target_process}' started, start recording...")
        # Call the screen recording function here
        break
    time.sleep(1)