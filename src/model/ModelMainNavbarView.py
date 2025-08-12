from data.main_model_codding_db import (
    dict_object_seralization,
)
from modules.RichText import RichText
from modules.nav_app_bar import nav_app_bar, nav_drawer_widget
from pages.main_menu import MainMenu


import flet as ft


class page_app_view(ft.View):
    """'
    ## Create frame view
    ```python
    >>> current_view = page_app_view(
    >>>                page = self.page,
    >>>                route = self.route,
    >>>                content = ft.ElevatedButton(
    >>>                    text = 'Home',
    >>>                    on_click = lambda _: self.page.go('/'),
    >>> ))
    ```
    """

    def __init__(
        self,
        page: object = None,
        route: str = str(),
        content: object = None,
        index_page: int = None,
        show_navigation: bool = False,
    ) -> None:
        super().__init__()
        self.page = page
        self.route = route
        self.padding = ft.padding.all(0)
        # self.padding = ft.padding.only(left=2, right=0, bottom=0, top=8)
        self.bgcolor = ft.Colors.GREY_900
        self.content = content
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.index_pages_dict: dict = {
            0: MainMenu(
                page=self.page,
                menu_list=dict_object_seralization(),
                go_to="/index_layer_one",
            ),
            1: MainMenu(
                page=self.page,
                show_fremeworks=True,
                menu_list=dict_object_seralization(),
                go_to="/index_layer_one",
            ),
        }

        self.controls: list = [
            (
                self.index_pages_dict.get(index_page)
                if not index_page == None
                else content
            ),
        ]

        if show_navigation:
            # self.appbar = ft.AppBar(
            #     title=ft.Text("Bottom AppBar Demo"),
            #     center_title=True,
            #     bgcolor=ft.Colors("grey900"),
            #     automatically_imply_leading=False,
            # )

            # self.floating_action_button_location = (
            #     ft.FloatingActionButtonLocation.MINI_END_TOP
            # )
            self.drawer = nav_drawer_widget(page=self.page)
            self.floating_action_button = ft.FloatingActionButton(
                icon=ft.Icons.QR_CODE_SCANNER_OUTLINED,
                bgcolor=ft.Colors("grey900"),
                mini=True,
                foreground_color=ft.Colors.AMBER_100,
                disabled_elevation=True,
                focus_elevation=0,
                on_click=lambda _: self.open_drawer(),
            )

            self.navigation_bar = ft.NavigationBar(
                selected_index=index_page,
                bgcolor=ft.Colors("grey900"),
                # offset=(0, -0.05),
                height=60,
                on_change=lambda _: self.change_screens(index_page=_.control),
                elevation=32,
                destinations=[
                    ft.NavigationBarDestination(
                        label="Learning",
                        icon=ft.Icons.MENU_BOOK_OUTLINED,
                        selected_icon=ft.Icons.MENU_BOOK_ROUNDED,
                    ),
                    ft.NavigationBarDestination(
                        label="Framewoks",
                        icon=ft.Icons.BARCODE_READER,
                        # selected_icon=ft.Icons.BARCODE_READER,
                    ),
                ],
            )
            self.appbar = nav_app_bar(
                page=self.page,
                visible=True,
                bgcolor=ft.Colors("grey900"),
                icon_left=ft.Icons.COMPOST_ROUNDED,
                icon_right=ft.Icons.TABLE_ROWS_ROUNDED,
                title="CodeHex",
                menu_drawer=self.drawer,
            )

    def open_drawer(self, drawer: object = None):
        dlg_modal = ft.AlertDialog(
            title=ft.Text(
                value="Open google drive",
                size=26,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD,
                font_family="Consolas",
            ),
            # adaptive=True,
            modal=True,
            inset_padding=ft.padding.symmetric(vertical=8, horizontal=0),
            content=ft.Container(
                border_radius=ft.border_radius.only(
                    top_left=24,
                    top_right=24,
                    bottom_left=24,
                    bottom_right=24,
                ),
                height=230,
                image=ft.DecorationImage(
                    src="qr_code.jpeg",
                    fit=ft.ImageFit.FILL,
                    # opacity=0.02,
                ),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
                alignment=ft.alignment.center,
                ink_color=ft.Colors("yellow"),
                bgcolor=ft.Colors("black12"),
            ),
            actions=[
                RichText(
                    page=self.page,
                    icon="cloud_download_rounded",
                    text="DOWNLOAD APK",
                    text_link="https://drive.google.com/drive/folders/1CqswYauQsm0JKnUpj-DXOWOiiSCDc0Ur",
                ),
                ft.ElevatedButton(
                    text="Closet",
                    bgcolor="red",
                    on_click=lambda _: self.page.close(dlg_modal),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.open(dlg_modal)

    def change_screens(self, index_page: int = None):
        dynamic_index: int = index_page.selected_index
        self.page.session.set("current_idex", dynamic_index)

        self.controls = [
            self.index_pages_dict.get(dynamic_index),
        ]
        self.update()
