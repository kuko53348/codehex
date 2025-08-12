import flet as ft

from modules.card_layer_two import CardLayerTwo


class PageOneMenu(ft.Container):

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
        self.padding = ft.padding.only(top=4, bottom=4)
        # top_left,top_center,top_right,center_lef,center,center_righ,bottom_left,bottom_right,bottom_center
        self.alignment = ft.alignment.top_center
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors("black12")
        self.ink_color = ft.Colors("yellow")

        self.content = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            spacing=0,
            run_spacing=0,
            controls=[
                CardLayerTwo(
                    page=self.page,
                    header=_,
                    sub_header=self.header,
                    image_decoration="icon.png",
                    go_to=go_to,
                )
                for _ in self.menu_list
            ],
        )
