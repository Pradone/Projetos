import pyautogui
import time

pyautogui.PAUSE = 0.5

def main_code():
    open_browser()
    RR()
                              
def open_browser():
    pyautogui.press("win")
    pyautogui.write("Chorme")
    pyautogui.press("enter")
    time.sleep(1)
    
def RR():
    time.sleep(0.25)
    pyautogui.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=0s")
    pyautogui.press("enter")
    
    
main_code()