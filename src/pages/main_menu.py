import flet as ft

from modules.card_layer_one import CardLayerOne


class MainMenu(ft.Container):

    def __init__(
        self, page: object = None, menu_list: dict = dict(), go_to: str = "/"
    ) -> None:
        super().__init__()
        self.page = page

        self.menu_list = menu_list.keys()
        # self.tooltip = 'Container'
        # self.image = self.image = ft.DecorationImage(src='logo.png',fit=ft.ImageFit.COVER,opacity=0.02)  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
        # self.border_radius = ft.border_radius.only(top_left = 8, top_right = 8, bottom_left = 8, bottom_right = 8)
        # self.gradient = ft.LinearGradient(begin = ft.alignment.top_center, end = ft.alignment.bottom_center,colors = [ft.Colors('transparent'), ft.Colors('black12'),],)
        # self.shadow = ft.BoxShadow(spread_radius = 1, blur_radius  = 15, color = ft.Colors('bluegrey300'), offset = ft.Offset(0,0), blur_style = ft.ShadowBlurStyle.OUTER,)
        # self.height = 150
        # self.width = 150
        # self.padding = ft.padding.only(left = 8, right = 8, bottom = 8, top = 8)
        # self.border_radius = ft.border_radius.only(top_left = 8, top_right = 8, bottom_left = 8, bottom_right = 8)
        # self.border = ft.border.all(width = 2, color = ft.Colors('black12'))
        # top_left,top_center,top_right,center_lef,center,center_righ,bottom_left,bottom_right,bottom_center
        self.alignment = ft.alignment.center
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors("black12")
        self.ink_color = ft.Colors("yellow")

        self.content = ft.GridView(
            expand=1,
            runs_count=2,
            max_extent=280,
            child_aspect_ratio=1.0,
            spacing=8,
            run_spacing=8,
            # wrap=True,
            controls=[
                CardLayerOne(
                    page=self.page,
                    image_decoration="icon.png",
                    go_to=go_to,
                    text_index=_,
                )
                for _ in self.menu_list
            ],
        )
