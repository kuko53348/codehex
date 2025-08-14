import flet as ft

from data.app_version_db import get_database
from modules.RichText import RichText


class nav_drawer_widget(ft.NavigationDrawer):

    dict_documentation: dict = {
        "0": "Gallery",
        "1": "Documentacion",
        "2": "Developer",
        "3": "App version",
    }

    def __init__(self, page: object = None):
        super().__init__()
        self.page = page
        self.shadow_color = "black"
        self.elevation = 24
        self.bgcolor = ("surface,0.96",)
        self.surface_tint_color = "black,0.4"
        self.indicator_color = "grey,0.25"
        self.controls = [
            ft.Container(
                padding=ft.padding.all(0),
                margin=ft.margin.all(0),
                alignment=ft.alignment.center,
                height=280,
                border_radius=ft.border_radius.only(
                    top_left=0, top_right=0, bottom_left=0, bottom_right=8
                ),
                border=ft.border.all(4, ft.Colors.SURFACE),
                content=ft.Image(
                    src="logo.png",
                    fit=ft.ImageFit.COVER,
                    # opacity=0.80,
                    expand=True,
                    scale=1.2,
                ),
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=22,
                    color=ft.Colors.BLACK,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                ),
            ),
            # ft.Divider(thickness=0.1),
            ft.Container(height=12),
            # ft.Container(
            #     expand=True,
            #     ink=False,
            #     bgcolor="TRANSPARENT",
            #     padding=ft.padding.all(8),
            #     margin=ft.margin.all(8),
            #     alignment=ft.alignment.center,
            #     content=ft.Text(
            #         value="CodeHex",
            #         text_align=ft.TextAlign.CENTER,
            #         weight=ft.FontWeight.BOLD,
            #         # italic            = True,
            #         size=18,
            #         font_family="Consolas",  # "Consolas ,RobotoSlab
            #     ),
            # ),
            ft.Divider(thickness=0.1),
            ft.NavigationDrawerDestination(
                label="Gallery",
                icon=ft.Icon(ft.Icons.CAMERA_OUTLINED),
                selected_icon=ft.Icons.CAMERA,
            ),
            ft.NavigationDrawerDestination(
                label="Documentation",
                icon=ft.Icons.AUTO_STORIES_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.AUTO_STORIES),
            ),
            ft.NavigationDrawerDestination(
                label="Developer",
                icon=ft.Icon(ft.Icons.CLEAN_HANDS_OUTLINED),
                selected_icon=ft.Icons.CLEAN_HANDS,
            ),
            ft.NavigationDrawerDestination(
                label="App version",
                icon=ft.Icon(ft.Icons.LOCAL_MALL_OUTLINED),
                selected_icon=ft.Icons.LOCAL_MALL,
            ),
        ]
        self.on_change = lambda e: self.handle_change(index_data=e)

    def handle_change(self, index_data):
        # MODEL OF DATA SELECTED
        self.model_data = self.dict_documentation.get(index_data.data)

        dlg_modal = ft.AlertDialog(
            title=ft.Text(value=self.model_data),
            # adaptive=True,
            modal=True,
            inset_padding=ft.padding.symmetric(vertical=12, horizontal=8),
            content=ft.Column(
                scroll="HIDDEN",
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    (
                        ft.Container()
                        if not self.model_data == "Developer"
                        else ft.Container(  #: [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                            border_radius=ft.border_radius.all(32),
                            image=ft.DecorationImage(
                                src="my_avatar.jpeg",
                                fit=ft.ImageFit.COVER,
                                # opacity=0.02,
                            ),  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
                            alignment=ft.alignment.center,
                            height=150,
                            width=150,
                            # ink = True,
                            ink_color=ft.Colors("yellow"),
                            expand=True,
                            bgcolor=ft.Colors("black12"),
                        )
                    ),
                    ft.Text(
                        size=12,
                        value=get_database(index=self.model_data),
                        text_align=ft.TextAlign.LEFT,
                    ),
                    RichText(
                        page=self.page,
                        icon="discord_rounded",
                        text="@legend_53348",
                        text_link="https://discord.com/channels/@me/@legend_53348",
                    ),
                    RichText(
                        page=self.page,
                        icon="developer_mode_rounded",
                        text="GitHub Repository",
                        text_link="https://github.com/kuko53348/codehex.git",
                    ),
                    RichText(
                        page=self.page,
                        icon="slow_motion_video",
                        text="Youtube channel",
                        text_link="https://www.youtube.com/@flet-box",
                    ),
                    RichText(
                        page=self.page,
                        icon="admin_panel_settings",
                        text="Apache License",
                        text_link="http://www.apache.org/licenses/",
                    ),
                ],
            ),
            actions=[
                ft.ElevatedButton(
                    text="Closet",
                    bgcolor="red",
                    on_click=lambda _: self.page.close(dlg_modal),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.page.open(dlg_modal)


class nav_app_bar(ft.AppBar):

    def __init__(
        self,
        page: object = object(),
        visible: bool = False,
        title: str = "",
        icon_left: str = "coffee_rounded",
        icon_right: str = "table_rows_rounded",
        menu_drawer: object = None,
        bgcolor: object = None,
    ):
        super().__init__()
        self.page = page
        self.visible = visible

        self.title = ft.Text(
            value=title,
        )
        self.bgcolor = bgcolor
        self.leading = ft.Icon(
            name=ft.Icons(icon_left),
        )
        self.center_title = False
        self.actions = [
            ft.IconButton(
                icon=ft.Icons(icon_right),
                on_click=lambda e: self.check_menu_bar(menu_drawer=menu_drawer),
            ),
        ]

    def check_menu_bar(self, menu_drawer: object = None):
        self.page.open(menu_drawer)
        self.page.update()
