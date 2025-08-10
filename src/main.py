import flet as ft

from data.main_model_codding_db import dict_object_seralization


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
            self.page.views.append(
                # page_app_view(
                #     page=self.page,
                #     route=self.route,
                #     content=ft.ElevatedButton(
                #         text="next",
                #         on_click=lambda _: self.page.go("/home"),
                #     ),
                # )
                ft.Container(
                    width=320,
                    height=320,
                    content=ft.Text(value=dict_object_seralization()["cpp"].code),
                )
            )
        if self.page.route == "/home":
            self.page.views.append(
                # page_app_view(
                #     page=self.page,
                #     route=self.route,
                #     content=ft.ElevatedButton(
                #         text="Home",
                #         on_click=lambda _: self.page.go("/"),
                #     ),
                # )
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
