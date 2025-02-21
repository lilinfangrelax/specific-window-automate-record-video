import pyautogui
import time

def activate_obs_window():
    obs_windows = pyautogui.getWindowsWithTitle("OBS 31") #  According OBS Studio window title to change
    if obs_windows:
        obs_window = obs_windows[0] #  Assume first window is OBS Studio
        obs_window.activate()
        print("Activated OBS Studio window")
        pyautogui.press("f3")
        time.sleep(1) #  Wait for window activated
        return True #
    else:
        print("Can't find OBS Studio window")
        return False

if __name__ == "__main__":
    activate_obs_window()
