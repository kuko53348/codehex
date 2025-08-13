import flet as ft


#  widget edit tag name
class CardLayerOne(ft.Container):

    def __init__(
        self,
        page: object = None,
        image_decoration: str = "",
        text_index: str = "",
        go_to: str = "/",
    ) -> None:
        super().__init__()
        self.page = page

        self.expand = True
        self.bgcolor = ft.Colors("transparent")
        self.alignment = ft.alignment.top_center
        self.padding = ft.padding.only(left=4, right=4, bottom=4, top=4)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)
        self.text_index = text_index
        # content of current widget
        self.content = ft.Container(
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            border_radius=ft.border_radius.all(32),
            padding=ft.padding.only(left=2, top=2, right=2, bottom=8),
            on_click=lambda _: self.go_to_next_page(go_to=go_to),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                run_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        expand=True,
                        padding=ft.padding.only(left=8, top=8, right=8, bottom=0),
                        border_radius=ft.border_radius.all(32),
                        width=340,
                        image=ft.DecorationImage(
                            src=image_decoration,
                            fit="cover",
                            opacity=0.8,
                        ),
                        bgcolor=ft.Colors("grey500"),
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            run_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(
                                        left=8, right=8, bottom=8, top=8
                                    ),
                                    bgcolor=ft.Colors.with_opacity(
                                        opacity=0.8, color=ft.Colors("grey900")
                                    ),
                                    border_radius=ft.border_radius.only(
                                        top_left=32,
                                        top_right=32,
                                        bottom_left=32,
                                        bottom_right=32,
                                    ),
                                    # expand=True,
                                    content=ft.Icon(
                                        name=ft.Icons.DATA_ARRAY_ROUNDED,
                                    ),
                                ),
                            ],
                        ),
                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        run_alignment=ft.CrossAxisAlignment.CENTER,
                        # expand=True,
                        height=24,
                        spacing=0,
                        run_spacing=0,
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    text_align=ft.TextAlign.LEFT,
                                    weight=ft.FontWeight.BOLD,
                                    font_family="Consolas",
                                    size=18,
                                    value=text_index,
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

    def go_to_next_page(self, go_to: object = None):
        # print(f"[+] Layer one: {self.text_index}")
        self.page.session.set("layer_one_selected", self.text_index)
        self.page.go(go_to)
