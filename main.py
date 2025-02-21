"""
Simple code matters. We should aim to achieve our goals as quickly as possible.

Requirement:
1. OBS Studio installed.
2. Record scene configured.
3. Hotkeys to start and stop recording.
"""
import psutil, time
import pyautogui
import sys


# default value, without command line input
target_process = "Notepad.exe"
obs_studio_start_record_hotkey = "f3"
obs_studio_stop_record_hotkey = "f4"
obs_studio_window_name = "OBS"
if len(sys.argv) == 5:
    target_process = sys.argv[1]
    obs_studio_start_record_hotkey = sys.argv[2]
    obs_studio_stop_record_hotkey = sys.argv[3]
    obs_studio_window_name = sys.argv[4]
obs_studio_recording = False
print("Script Started.")

def check_process(process_name):
    """Check whether the specified process is started"""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False


while True:
    if check_process(target_process) and not obs_studio_recording:
        print(f"Detected '{target_process}' started, start recording...")
        obs_windows = pyautogui.getWindowsWithTitle(obs_studio_window_name)
        if obs_windows:
            obs_window = obs_windows[0]
            obs_window.activate()
            pyautogui.press(obs_studio_start_record_hotkey)
            obs_studio_recording = True
    if not check_process(target_process) and obs_studio_recording:
        print(f"Detected '{target_process}' terminated, stop recording...")
        obs_windows = pyautogui.getWindowsWithTitle(obs_studio_window_name)
        if obs_windows:
            obs_window = obs_windows[0]
            obs_window.activate()
            pyautogui.press(obs_studio_stop_record_hotkey)
            obs_studio_recording = False
    if obs_studio_recording:
        time.sleep(10)
    time.sleep(3)