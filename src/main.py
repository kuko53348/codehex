import flet as ft

from data.main_model_codding_db import dict_object_seralization
from model.ModelPageView import ModelPageView
from model.ModelMainNavbarView import page_app_view
from pages.page_one_menu import PageOneMenu
from pages.main_menu import MainMenu
from pages.markdown_page_view import MarkDownPageView
from pages.page_two_menu import PageTwoMenu


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

        # self.page.go("/")
        self.page.go("/home")
        # self.page.go("/index_layer_two")

    def on_route_change(self, page: object = None, route: str = str()) -> None:
        self.page = page
        self.route = route
        self.page.views.clear()

        if self.page.route == "/":
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    content=ft.ElevatedButton(
                        text="next",
                        on_click=lambda _: self.page.go("/home"),
                    ),
                    # content=ft.Text(value=dict_object_seralization()["cpp"].code),
                )
            )

        elif self.page.route == "/home":
            # first code index
            self.page.views.append(
                page_app_view(
                    page=self.page,
                    route=self.route,
                    show_navigation=True,
                    content=MainMenu(
                        page=self.page,
                        menu_list=dict_object_seralization(),
                        go_to="/index_layer_one",
                    ),
                    # content=ft.Text(value=dict_object_seralization()["cpp"].code),
                )
            )
        elif self.page.route == "/index_layer_one":
            header = self.page.session.get("layer_one_selected")
            self.page.views.append(
                ModelPageView(
                    page=self.page,
                    title_page=header,
                    back_click=lambda widget: self.page.go("/home"),
                    content=PageOneMenu(
                        page=self.page,
                        header=header,
                        menu_list=dict_object_seralization()[header].__dict__,
                        go_to="/index_layer_two",
                    ),
                )
            )
        elif self.page.route == "/index_layer_two":
            header = self.page.session.get("layer_one_selected")
            layer_two_selected = self.page.session.get("layer_two_selected")
            code = dict_object_seralization()[header].__dict__[layer_two_selected]

            self.page.views.append(
                ModelPageView(
                    page=self.page,
                    title_page=layer_two_selected,
                    back_click=lambda widget: self.page.go("/index_layer_one"),
                    content=PageTwoMenu(
                        page=self.page,
                        header=layer_two_selected,
                        menu_list=code,
                        go_to="/markdown",
                    ),
                )
            )

        elif self.page.route == "/markdown":
            header = self.page.session.get("layer_one_selected")
            layer_two_selected = self.page.session.get("layer_two_selected")
            layer_three_selected = self.page.session.get("layer_three_selected")
            code = dict_object_seralization()[header].__dict__[layer_two_selected][
                layer_three_selected
            ]

            self.page.views.append(
                MarkDownPageView(
                    page=self.page,
                    md_code=code,
                    text_header=layer_three_selected,
                    image_theme=f"{header}.jpeg",
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
