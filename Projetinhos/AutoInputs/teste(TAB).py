import flet as ft
import pyautogui as pa
import keyboard as key
import time

stop_autoClick = False
startBugfix = False

def main(pag):
    tittle = ft.Text("Autoclicker", size=25, weight=ft.FontWeight.BOLD)

    def start_autoClick(event):
        global stop_autoClick, startBugfix
        is_show = False
        
        enable_text = ft.Text("The autoclicker is ",
                              size=15,
                              weight=ft.FontWeight.BOLD)
        enable_text2 = ft.Text("enabled",
                               size=15,
                               weight=ft.FontWeight.BOLD,
                               color=ft.colors.GREEN)
        
        if startBugfix == False:
            pag.add(enable_text, enable_text2)
            startBugfix = True
            is_show = True
        
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
        if is_show == True and startBugfix == False:
            pag.remove(enable_text, enable_text2)

    def end_autoClick(event):
        global stop_autoClick, startBugfix
        stop_autoClick = True
        startBugfix = False
        pag.update()

    
    configButton = ft.IconButton(
                                ft.icons.SETTINGS,
                                icon_size=15,
                                icon_color=ft.colors.WHITE,                                
                                width=30,
                                height=30)
    
    configButtonLayout = ft.Row(
        controls=[
            ft.Container(content=configButton, alignment=ft.alignment.center)
        ],
        alignment=ft.MainAxisAlignment.START
    )
    
    start_button = ft.ElevatedButton("Start", on_click=start_autoClick, color=ft.colors.GREEN)
    end_button = ft.ElevatedButton("Stop", on_click=end_autoClick, color=ft.colors.RED)
    buttons = ft.Row([start_button, end_button])
    tab1 = ft.Column([ft.Container(content=tittle, padding=2), buttons], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    pag.title = "PyClick"
    pag.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pag.theme_mode = "dark"
    pag.window_minimizable = False
    pag.window_maximizable = False
    pag.window_resizable = True
    pag.padding = 1
    pag.window_width = 200
    pag.window_height = 300
    
    
    
    table = ft.Tabs(
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Click",
                content=tab1
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SETTINGS, color=ft.colors.WHITE, size=15),
                content=ft.Text("This is Tab 2"),
            )
        ], tab_alignment=ft.TabAlignment.START
    )
    
    pag.add(table)


ft.app(main)

# add some additional functions