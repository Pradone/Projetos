import pyautogui
import time

pyautogui.PAUSE = 0.5

#Open Chrome
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

#Search Magister
time.sleep(2.5)
pyautogui.write("https://wwws.unit.br/Portal/Index.jsp")
pyautogui.press("enter")

#Adding the login
time.sleep(0.5)
pyautogui.write("usuario")

#Adding the password
time.sleep(0.5)
pyautogui.press('tab')
pyautogui.write("senha")
pyautogui.press("enter")
