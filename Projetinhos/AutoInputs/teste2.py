import flet as ft

def main(page: ft.Page):
    page.title = "Exemplo de Redimensionamento de Switch"
    page.padding = 20  # Adiciona padding para a página

    # Criar um contêiner com tamanho customizado contendo o switch
    custom_switch_container = ft.Container(
        content=ft.Switch(
            value=False,
            label="Switch Redimensionado",
            on_change=lambda e: print("Switch valor:", e.control.value),
        ),
        width=100,  # Largura do contêiner
        height=50,  # Altura do contêiner
        alignment=ft.alignment.center  # Alinha o switch no centro do contêiner
    )

    # Adicionar o contêiner com o switch redimensionado à coluna
    column = ft.Column(
        controls=[custom_switch_container],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Adicionar a coluna à página
    page.add(column)

# Inicializar a aplicação
ft.app(target=main)
