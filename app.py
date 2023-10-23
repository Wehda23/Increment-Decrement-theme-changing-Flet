import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent






def main(page: ft.page) -> None:
    page.title = "increment counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'dark'

    text_number: TextField = TextField(value = '0', text_align= ft.TextAlign.CENTER, width = 100)

    def decrement(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        page.update()
    
    def increment(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1)
        page.update()
    def change_theme(e: ControlEvent) -> None:
        page.theme_mode = 'dark' if page.theme_mode == 'light' else 'light'
        e.control.selected = not e.control.selected
        page.update()
    page.add(
        ft.Row(
            [
            ft.IconButton(ft.icons.REMOVE, on_click=decrement),
            text_number,
            ft.IconButton(ft.icons.ADD, on_click=increment),
            ft.IconButton(icon = ft.icons.LIGHT_MODE ,selected_icon= ft.icons.DARK_MODE, on_click=change_theme, selected = False),
            ],
            alignment=ft.MainAxisAlignment.CENTER,

        )
    )

if __name__ == "__main__":
    print("Debugging")
    ft.app(target = main)
    #ft.app(target = main, view = ft.AppView.WEB_BROWSER)