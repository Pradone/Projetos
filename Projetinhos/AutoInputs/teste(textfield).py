import flet as ft
from time import sleep


def main(pag):
    
    def timer(event):
        try:
            if int(cps.value) >= 101:
                print("maior que 100 nao pode")
            elif int(cps.value) <= 0:
                print("menor que 1 nao pode")
            else:
                for numTimer in range(1,(100 + 1)):
                    
                    
                    textoTimer.value = numTimer
                    print(int(cps.value) + int(cps.value))
                    
                    sleep(1 / int(cps.value))
                    pag.update()
        except ValueError:
            print("valor invalido")
    
    
    textoTimer = ft.Text("")
    
    cps = ft.TextField(on_submit=timer,width=100, height= 25, text_size= 15,text_vertical_align=-0.6, border_color=ft.colors.WHITE, show_cursor=False)
    
    botaLegal =  ft.ElevatedButton("Start", on_click=timer)
    
    cpStyled = ft.Row([
        ft.Container(content=cps),
        ft.Container(content=botaLegal)
        ])
    
    
    pag.title = "Teste3"
    pag.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pag.theme_mode = "dark"
    pag.window_minimizable = False
    pag.window_maximizable = False
    pag.window_resizable = False
    pag.padding = 1
    pag.window_width = 210
    pag.window_height = 250
    
    pag.add(cpStyled, textoTimer)

ft.app(main)