import flet as ft
import pyautogui as pa
import keyboard as key
from time import sleep

stop_autoClick = False
startBugfix = False
cpsVal = 100

def main(pag):
    title = ft.Text("Autoclicker", size=25, weight=ft.FontWeight.BOLD)

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
        
        def clicking():
            sleep(1/cpsVal)
            pa.click()
            
        while True:
            if key.is_pressed('F4'):
                sleep(0.25)
                while True:  
                    if key.is_pressed('F4'):
                        sleep(0.25)
                        break
                    else:
                        clicking()
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
        
        
        
        
    def config(event):
        global configtitle, userInput, saveButton, cpStyled, cps
        try:
            pag.remove(title, buttons)
            
            configtitle = ft.Text("Configuration", size=25, weight=ft.FontWeight.BOLD)
            def theme_changed(event):            
                pag.theme_mode = (
                    ft.ThemeMode.DARK
                    if pag.theme_mode == ft.ThemeMode.LIGHT
                    else ft.ThemeMode.LIGHT
                )
                swh1.label = ("Light theme" if pag.theme_mode == ft.ThemeMode.LIGHT else "Dark theme")
                swh1.value = (True if pag.theme_mode == ft.ThemeMode.LIGHT else False)
                btn1.color = (ft.colors.BLACK if pag.theme_mode == ft.ThemeMode.LIGHT else ft.colors.WHITE)
                
                
                
                clickButton.icon_color = (ft.colors.BLACK if pag.theme_mode == ft.ThemeMode.LIGHT else ft.colors.WHITE)
                configButton.icon_color = (ft.colors.BLACK if pag.theme_mode == ft.ThemeMode.LIGHT else ft.colors.WHITE)
                pag.update()
                
                
            def save(event):
                global cpsVal
                
                btn1.text = "Saved"
                btn1.color = ft.colors.GREEN_ACCENT
                
                cpsVal = int(cps.value)
            
                pag.update()
            
                
            swh1 = ft.Switch(label="Dark theme", on_change=theme_changed, value=False)
            swh1.label = ("Light theme" if pag.theme_mode == ft.ThemeMode.LIGHT else "Dark theme")
            swh1.value = (True if pag.theme_mode == ft.ThemeMode.LIGHT else False)
            
            
            cps = ft.TextField(value=cpsVal, on_submit=save, width=100, height= 25, text_size= 15,text_vertical_align=-0.6, border_color=ft.colors.WHITE, show_cursor=False)
            
            
            btn1 = ft.ElevatedButton("Save", color=ft.colors.WHITE, on_click=save)
            btn1.color = (ft.colors.BLACK if pag.theme_mode == ft.ThemeMode.LIGHT else ft.colors.WHITE)
            
            userInput = ft.Column([swh1])
            cpStyled = ft.Row([
                ft.Container(content=cps),
                ft.Text("Cps")
            ])
            saveButton = ft.Row(
                controls=[
                    ft.Container(content=btn1, alignment=ft.alignment.center, padding=5)
                ], alignment=ft.MainAxisAlignment.END)
            
            
            pag.add(configtitle, userInput, cpStyled, saveButton)
            pag.window_width = 210
            pag.window_height = 300
        except ValueError:
            pass
            
        pag.update()
        
        
    def click(event):
        global configtitle, userInput
        try:
            pag.remove(configtitle, userInput, saveButton, cpStyled)
            
            
            pag.add(title, buttons)
            pag.window_width = 210
            pag.window_height = 250
        except ValueError:
            pass
        
        pag.update()
        
        
    
    
    configButton = ft.IconButton(ft.icons.SETTINGS,
                                icon_size=15,
                                icon_color=ft.colors.WHITE,                                
                                width=30,
                                height=30,
                                on_click=config)
    
    clickButton = ft.IconButton(ft.icons.ADS_CLICK_OUTLINED,
                                icon_size=15,
                                icon_color=ft.colors.WHITE,                                
                                width=30,
                                height=30,
                                on_click=click)
    topButtonLayout = ft.Row(
        controls=[
            ft.Container(content=clickButton, alignment=ft.alignment.center),
            ft.Container(content=configButton, alignment=ft.alignment.center)
        ], alignment=ft.MainAxisAlignment.START)
    
    start_button = ft.ElevatedButton("Start", on_click=start_autoClick, color=ft.colors.GREEN)
    end_button = ft.ElevatedButton("Stop", on_click=end_autoClick, color=ft.colors.RED)
    buttons = ft.Row([start_button, end_button], alignment=ft.MainAxisAlignment.CENTER)

    pag.title = "PyClick"
    pag.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pag.theme_mode = "dark"
    pag.window_minimizable = False
    pag.window_maximizable = False
    pag.window_resizable = False
    pag.padding = 1
    pag.window_width = 210
    pag.window_height = 250

    pag.add(topButtonLayout, title, buttons)


ft.app(main)

# embelezar a aba de config
# corrigir bug do 1 segundo
