# from database.guantanamera_db import get_database


import flet as ft


class RichText(ft.Row):

    def __init__(
        self,
        page: object = None,
        icon: object = None,
        text: str = "",
        text_link: str = "",
    ) -> None:
        super().__init__()
        self.page = page
        self.alignment = ft.MainAxisAlignment.START
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.run_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
        self.spacing = 8
        self.run_spacing = 8
        self.controls = [
            ft.Icon(name=icon),
            ft.Text(
                disabled=False,
                spans=[
                    ft.TextSpan(
                        text,
                        ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                        url=text_link,
                        on_enter=lambda data_one: self.highlight_link(
                            data_pased=data_one
                        ),
                        on_exit=lambda data_two: self.unhighlight_link(
                            data_pased=data_two
                        ),
                    ),
                ],
            ),
        ]

    def highlight_link(self, data_pased: object = None):
        data_pased.control.style.color = ft.Colors.BLUE
        data_pased.control.update()

    def unhighlight_link(self, data_pased: object = None):
        data_pased.control.style.color = None
        data_pased.control.update()
