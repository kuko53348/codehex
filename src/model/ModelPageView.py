import flet as ft


class ModelPageView(ft.View):

    def __init__(
        self,
        page: object = None,
        content: object = None,
        back_click: object = None,
        title_page: str = "Code page",
    ) -> None:
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(bottom=12)
        self.controls_widgets = content
        self.appbar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK, icon_size=24, on_click=back_click
            ),
            title=ft.Text(
                expand=True,
                value=title_page,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
            ),
            bgcolor=ft.Colors.GREY_900,
        )
        self.vertical_alignment = ft.MainAxisAlignment.START
        self.horizontal_alignment = ft.CrossAxisAlignment.START

        self.expand = True
        self.bgcolor = ft.Colors("grey900")
        self.navigation_bar = ft.NavigationBar(
            selected_index=0,
            bgcolor=ft.Colors("grey900"),
            height=60,
            on_change=lambda _: self.page.go("/home"),
            elevation=32,
            destinations=[
                ft.NavigationBarDestination(
                    label="Starters",
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME_ROUNDED,
                ),
            ],
        )
        self.controls = [self.controls_widgets]
