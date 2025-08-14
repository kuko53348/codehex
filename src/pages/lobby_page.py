import flet as ft

from data.app_version_db import get_database


class LobbyPage(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.image = self.image = ft.DecorationImage(
            src="logo.png", fit=ft.ImageFit.COVER, opacity=0.08
        )  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
        self.alignment = ft.alignment.center
        self.padding = ft.padding.only(left=24, right=24, bottom=84, top=84)
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors("black12")
        self.ink_color = ft.Colors("yellow")

        self.content = ft.Container(
            blur=(8, 12),
            expand=False,
            # width=640,
            # height=520,
            padding=ft.padding.only(left=24, right=24, bottom=24, top=24),
            # margin=ft.margin.only(left=8, right=8, bottom=54, top=54),
            border_radius=ft.border_radius.only(
                top_left=24, top_right=24, bottom_left=24, bottom_right=24
            ),
            border=ft.border.all(
                width=2,
                color=ft.Colors.with_opacity(opacity=0.08, color=ft.Colors.WHITE),
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[
                    ft.Colors.TRANSPARENT,
                    ft.Colors.BLACK12,
                    ft.Colors.BLACK26,
                    ft.Colors.BLACK38,
                    ft.Colors.BLACK45,
                ],
            ),
            content=ft.Column(
                # ft.MainAxisAlignment START END CENTER SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                # ft.CrossAxisAlignment START END CENTER STRETCH BASELINE
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                expand=False,
                spacing=8,
                run_spacing=8,
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text(
                                value="CodeHex",
                                size=48,
                                text_align=ft.TextAlign.CENTER,
                                weight=ft.FontWeight.BOLD,
                                font_family="Consolas",
                            ),
                            ft.Text(
                                value="CodeHex",
                                text_align=ft.TextAlign.CENTER,
                                size=28,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(value=get_database("CodexLobby")),
                        ]
                    ),
                    ft.FloatingActionButton(
                        icon=ft.Icons.ARROW_RIGHT_OUTLINED,
                        bgcolor=ft.Colors("grey900"),
                        mini=True,
                        foreground_color=ft.Colors.AMBER_100,
                        disabled_elevation=True,
                        focus_elevation=0,
                        on_click=lambda _: self.page.go("/home"),
                    ),
                ],
            ),
        )
