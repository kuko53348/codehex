import flet as ft

from modules.card_layer_three import CardLayerThree


class PageTwoMenu(ft.Container):

    def __init__(
        self,
        page: object = None,
        menu_list: dict = dict(),
        go_to: str = "/",
        header: str = "",
    ) -> None:
        super().__init__()
        self.page = page

        self.menu_list = menu_list.keys()
        self.header = header
        self.padding = ft.padding.only(left=8, right=8, bottom=8, top=8)
        # self.border = ft.border.all(width = 2, color = ft.Colors('black12'))
        # top_left,top_center,top_right,center_lef,center,center_righ,bottom_left,bottom_right,bottom_center
        self.alignment = ft.alignment.top_center
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors("black12")
        self.ink_color = ft.Colors("yellow")

        self.content = ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            # expand=1,
            # runs_count=2,
            # max_extent=280,
            # child_aspect_ratio=1.0,
            # spacing=8,
            # run_spacing=8,
            # wrap=True,
            controls=[
                CardLayerThree(
                    page=self.page,
                    header=_,
                    sub_header=self.header,
                    image_decoration="icon.png",
                    go_to=go_to,
                )
                for _ in self.menu_list
            ],
        )
