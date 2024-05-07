import pyautogui
import time

pyautogui.PAUSE = 0.5

#Open Chrome
pyautogui.press('win')
pyautogui.write("Chrome")
pyautogui.press('enter')

#Search Ava
time.sleep(2.5)
pyautogui.write("https://ava.grupotiradentes.com/shared/online/login.html")
pyautogui.press('enter')

#Adding the login
time.sleep(0.5)
#in case of bugs
#pyautogui.click(x=946, y=308)
pyautogui.hotkey('ctrl','a')
pyautogui.press('del')
pyautogui.write("1231110608")

#Adding the password
time.sleep(0.5)
pyautogui.press('tab')
pyautogui.hotkey('ctrl','a')
pyautogui.press('del')
pyautogui.write("9e380209")
pyautogui.press('enter')