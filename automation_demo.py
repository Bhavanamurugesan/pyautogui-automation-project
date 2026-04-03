import pyautogui
import subprocess
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

def open_notepad():
    subprocess.Popen("notepad.exe")
    time.sleep(2)

def type_case_notes():
    pyautogui.write("Customer Support Automation Demo", interval=0.04)
    pyautogui.press("enter")
    pyautogui.press("enter")

    pyautogui.write(f"Run Time: {datetime.now()}", interval=0.04)
    pyautogui.press("enter")

    pyautogui.write("Customer ID: CX1001", interval=0.04)
    pyautogui.press("enter")

    pyautogui.write("Customer Name: Rahul Sharma", interval=0.04)
    pyautogui.press("enter")

    pyautogui.write("Issue: Login problem", interval=0.04)
    pyautogui.press("enter")

    pyautogui.write("Status: Resolved", interval=0.04)

def save_file():
    pyautogui.hotkey("ctrl", "s")
    time.sleep(2)
    pyautogui.write("customer_case_demo.txt", interval=0.04)
    pyautogui.press("enter")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("automation_proof.png")

def close_notepad():
    pyautogui.hotkey("alt", "f4")

def main():
    print("Automation starting in 5 seconds...")
    time.sleep(5)

    open_notepad()
    type_case_notes()
    save_file()
    take_screenshot()
    close_notepad()

    print("Automation completed.")

if __name__ == "__main__":
    main()