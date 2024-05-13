import flet as ft
import pyautogui as pa
import keyboard as key
import time

stop_autoClick = False
def main(pag):
    tittle = ft.Text("Autoclicker", size=25, weight=ft.FontWeight.BOLD)
    
    def start_autoClick(event):
        global stop_autoClick
        enable_text = ft.Text("The autoclicker is ",
                            size=15,
                            weight=ft.FontWeight.BOLD)
        enable_text2 = ft.Text("enabled",
                            size=15,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.GREEN)
        pag.add(enable_text,enable_text2)
        stop_autoClick = False
        while True:
            if key.is_pressed('F4'):
                time.sleep(0.25)
                while True:
                    if key.is_pressed('F4'): 
                        time.sleep(0.25)
                        break
                    else:
                        pa.click()
            if stop_autoClick == True:
                break
            pag.update()
        pag.remove(enable_text, enable_text2)

    def end_autoClick(event):
        global stop_autoClick
        stop_autoClick = True
        pag.update()

    start_button = ft.ElevatedButton("Start", on_click=start_autoClick, color=ft.colors.GREEN)
    end_button = ft.ElevatedButton("End", on_click=end_autoClick, color=ft.colors.RED)
    buttons = ft.Row([start_button, end_button])
    
    pag.title = "PyClick"
    pag.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pag.theme_mode = "dark"
    pag.window_minimizable = False
    pag.window_maximizable = False
    pag.window_resizable = False
    pag.window_width = 200
    pag.window_height = 200
    pag.add(tittle, buttons)
ft.app(main)


#add some additional functions