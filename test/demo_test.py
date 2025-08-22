import flet as ft


import flet as ft


#  widget edit tag name
class TextSearch(ft.Container):

    def __init__(
        self, page: object = None, list_filter: list = list(), debug: bool = False
    ) -> None:
        super().__init__()
        self.page = page
        self.debug = debug
        self.list_filter = list_filter
        self.text_box_visible = False
        self.search_text: str = str()

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

    def return_text(self, text: str = "") -> str:
        if self.debug:
            print(text)
        return text


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
        self, page: object = None, route: str = str(), content: object = None
    ) -> None:
        super().__init__()
        self.page = page
        self.route = route
        self.padding = 0
        self.content = content
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.controls: list = [self.content]


class flet_box_app:

    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window.left = 3
        self.page.window.top = 3
        self.page.padding = 0
        self.page.spacing = 0
        self.page.window.height = 720
        self.page.window.width = 320

        self.page.on_route_change = lambda _: self.on_route_change(
            page=self.page,
            route="/",
        )

        self.page.go("/")

    def on_route_change(self, page: object = None, route: str = str()) -> None:
        self.page = page
        self.route = route
        self.page.views.clear()

        if self.page.route == "/":
            demo_text = TextSearch(
                page=self.page,
                list_filter=["hello", "hallo", "maenys", "more"],
            )
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=demo_text,
                )
            )
        if self.page.route == "/home":
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=ft.ElevatedButton(
                        text="Home",
                        on_click=lambda _: self.page.go("/"),
                    ),
                )
            )

        self.page.update()


if __name__ == "__main__":
    ft.app(
        target=flet_box_app,
        assets_dir="assets",
        # name = 'Flet-Box',
        # route_url_strategy = 'assets/project_assets/',
        # use_color_emoji = True,
        # web_renderer = ft.WebRenderer.CANVAS_KIT,
        # port = 8081,
    )
