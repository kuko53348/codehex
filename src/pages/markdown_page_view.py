import flet as ft

from modules.markdown_code_editor import code_editor


class MarkDownPageView(ft.View):

    def __init__(
        self,
        page: object = None,
        content: object = None,
        md_code: str = "",
        text_header: str = "",
        image_theme: str = "logo.png",
    ) -> None:
        super().__init__()
        self.page = page
        self.padding = ft.padding.only(bottom=12)
        self.appbar = ft.AppBar(
            leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_size=24,
                on_click=lambda widget: self.page.go("/index_layer_two"),
            ),
            title=ft.Text(
                expand=True,
                size=14,
                value=text_header,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
            ),
            bgcolor=ft.Colors.GREY_900,
        )
        self.data = ft.View()
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # self.foreground_decoration = ft.BoxDecoration(
        #     image=ft.DecorationImage(
        #         src="card_shoppin_add.png", fit=ft.ImageFit.COVER, opacity=0.08
        #     )
        # )

        self.expand = True
        # bottom_appbar=ft.BottomAppBar(bgcolor=ft.Colors.GREY_900),
        self.bgcolor = "#282828"
        self.controls = [
            ft.Container(
                alignment=ft.alignment.center,
                # height=150,
                # width = 150,
                # ink = True,
                ink_color=ft.Colors("yellow"),
                expand=True,
                content=code_editor(
                    visible=True,
                    show_bar_cody=True,
                    page=self.page,
                    image_theme=image_theme,
                    md_code=md_code,
                ),
            ),
            ft.Container(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            tooltip="Home",
                            padding=ft.padding.all(0),
                            margin=ft.margin.all(0),
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        bgcolor=ft.Colors.with_opacity(
                                            opacity=0.2, color="cyan"
                                        ),
                                        icon="home",
                                        on_click=lambda widget: self.page.go("/home"),
                                    ),
                                ]
                            ),
                        ),
                    ],
                ),
            ),
        ]
