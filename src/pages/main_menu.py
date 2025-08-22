import flet as ft

from data.main_model_codding_db import show_only_frameworks
from modules.card_layer_one import CardLayerOne
from modules.text_search import TextSearch


class MainMenu(ft.Container):

    def __init__(
        self,
        page: object = None,
        menu_list: dict = dict(),
        go_to: str = "/",
        show_fremeworks: bool = False,
    ) -> None:
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.expand = True
        self.ink = True
        self.bgcolor = ft.Colors("black12")
        self.ink_color = ft.Colors("yellow")
        self.content = ft.Column(
            # spacing=8,
            # run_spacing=8,
            controls=[
                TextSearch(
                    page=self.page, list_filter=menu_list, debug=False, go_to=go_to
                ),
                ft.GridView(
                    expand=1,
                    runs_count=2,
                    max_extent=280,
                    child_aspect_ratio=1.0,
                    spacing=0,
                    run_spacing=0,
                ),
            ],
        )

        if show_fremeworks:
            for _ in show_only_frameworks():
                self.content.controls[1].controls.append(
                    CardLayerOne(
                        page=self.page,
                        image_decoration=f"{_}.jpeg",
                        go_to=go_to,
                        text_index=_,
                    )
                )
        else:
            for _ in show_only_frameworks():
                del menu_list[_]

            for _ in menu_list.keys():
                self.content.controls[1].controls.append(
                    CardLayerOne(
                        page=self.page,
                        image_decoration=f"{_}.jpeg",
                        go_to=go_to,
                        text_index=_,
                    )
                )
