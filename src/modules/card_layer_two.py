import flet as ft


class CardLayerTwo(ft.Container):

    def __init__(
        self,
        page: object = None,
        image_decoration: str = "",
        go_to: str = "/",
        header: str = "",
        sub_header: str = "",
    ) -> None:
        super().__init__()
        self.page = page

        self.header = header
        self.sub_header = sub_header

        self.expand = True
        self.bgcolor = ft.Colors("transparent")
        self.alignment = ft.alignment.top_center
        self.padding = ft.padding.only(left=4, right=4, bottom=4, top=4)
        self.margin = ft.margin.only(left=0, right=0, bottom=0, top=0)

        # content of current widget
        self.content = ft.Container(
            width=340,
            bgcolor=ft.Colors("grey900"),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors("black"),
                offset=ft.Offset(0, 5),
            ),
            border=ft.border.only(
                left=ft.border.BorderSide(8, "green"),
                top=None,
                right=None,
                bottom=None,
            ),
            on_click=lambda _: self.go_to_next_page(go_to=go_to),
            border_radius=ft.border_radius.all(12),
            padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
            content=ft.Column(
                controls=[
                    # Banner Title
                    ft.Text(
                        value=self.header,
                        size=14,
                        weight="bold",
                        color=ft.Colors("white"),
                    ),
                    # Banner Description
                    ft.Text(
                        value=self.sub_header,
                        size=11,
                        color=ft.Colors("white70"),
                    ),
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
        )

    def go_to_next_page(self, go_to: str = ""):
        # print(f"[+] Layer two: {self.header}")
        self.page.session.set("layer_two_selected", self.header)
        self.page.go(go_to)
