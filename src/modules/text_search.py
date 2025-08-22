import flet as ft


class TextSearch(ft.Container):

    def __init__(
        self,
        page: object = None,
        list_filter: list = list(),
        debug: bool = False,
        padding=ft.padding.all(8),
        go_to: str = str(),
    ) -> None:
        super().__init__()
        self.page = page
        self.debug = debug
        self.padding = padding
        self.list_filter = list_filter
        self.text_box_visible = False
        self.search_text: str = str()
        self.padding = ft.padding.all(8)
        self.go_to = go_to
        # content of current widget
        self.content = ft.Column(
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.Colors("transparent"),
                    alignment=ft.alignment.top_center,
                    padding=ft.padding.only(left=0, right=0, bottom=0, top=0),
                    margin=ft.margin.only(left=0, right=0, bottom=0, top=0),
                    content=ft.Container(
                        padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                        border_radius=ft.border_radius.all(24),
                        expand=True,
                        bgcolor=ft.Colors("grey900"),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors("black"),
                            offset=ft.Offset(0, 5),
                        ),
                        content=ft.Row(
                            controls=[
                                ft.TextField(
                                    expand=True,
                                    bgcolor="black12",
                                    label="Search",
                                    hint_text="Fill correct data",
                                    border_width=0,
                                    border_radius=ft.border_radius.all(18),
                                    border_color=ft.Colors("transparent"),
                                    on_change=lambda _: self.add_search(
                                        text_typed=_.data
                                    ),
                                    on_submit=lambda _: self.find_text(),
                                ),
                                ft.Container(
                                    border_radius=ft.border_radius.all(18),
                                    bgcolor=ft.Colors.with_opacity(
                                        opacity=0.8,
                                        color=ft.Colors("blue"),
                                    ),
                                    padding=ft.padding.all(8),
                                    content=ft.Icon(name="search"),
                                    on_click=lambda _: self.find_text(),
                                ),
                            ],
                        ),
                    ),
                ),
                ft.Container(
                    # expand=True,
                    visible=self.text_box_visible,
                    bgcolor=ft.Colors("transparent"),
                    alignment=ft.alignment.top_center,
                    padding=ft.padding.only(left=0, right=0, bottom=0, top=0),
                    margin=ft.margin.only(left=0, right=0, bottom=0, top=0),
                    content=ft.Container(
                        padding=ft.padding.only(left=8, top=8, right=8, bottom=8),
                        border_radius=ft.border_radius.all(12),
                        # border_radius=ft.border_radius.all(24),
                        expand=True,
                        bgcolor=ft.Colors("grey900"),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.Colors("black"),
                            offset=ft.Offset(0, 5),
                        ),
                        content=ft.Column(
                            expand=True,
                            spacing=0,
                            run_spacing=0,
                            controls=[],
                        ),
                    ),
                ),
            ]
        )

    def visible_widget(self, visible: bool = False):
        self.content.controls[1].visible = visible

    def update_widget(self):
        self.content.controls[1].update()

    def clean_widget(self):
        self.content.controls[1].content.content.controls.clear()
        self.visible_widget(visible=False)
        self.update_widget()

    def add_search(self, text_typed: str = ""):
        self.clean_widget()
        self.search_text = text_typed

    def find_text(self):
        self.clean_widget()

        for _ in self.list_filter:
            if _.startswith(self.search_text):
                self.content.controls[1].content.content.controls.append(
                    ft.ListTile(
                        # title=ft.Text(value=self.search_text),
                        title=ft.Text(value=_),
                        on_click=lambda _: self.return_text(text=_.control.title.value),
                        data=self.search_text,
                    )
                )

        if len(self.search_text) > 0:
            self.visible_widget(visible=True)
        else:
            self.visible_widget(visible=False)

        if not len(self.content.controls[1].content.content.controls) == 0:
            self.update_widget()

    def return_text(self, text: str = ""):
        if self.debug:
            print(text)

        self.page.session.set("layer_one_selected", text)
        self.page.go(self.go_to)
