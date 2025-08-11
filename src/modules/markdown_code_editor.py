import flet as ft
import time


class alert_dialog(ft.Container):

    def __init__(self, page: object = None, content: object = None) -> None:
        super().__init__()
        self.page = page
        self.alignment = ft.alignment.center
        self.ink = True
        self.visible = False
        self.ink_color = ft.Colors("yellow")
        self.border_radius = ft.border_radius.only(
            top_left=32, top_right=32, bottom_left=32, bottom_right=32
        )
        self.width = 200

        self.bgcolor = ft.Colors("red")
        self.content = ft.Text(value="Sussefully copied", weight="bold", size=13)


class code_editor(ft.Container):
    opacity_markdown: float = 0.9

    def __init__(
        self,
        widget: object = None,
        md_code: str = str(),
        visible: bool = False,
        show_bar_cody: bool = False,
        page: object = None,
        image_theme: str = "splash_android.png",
    ):
        super().__init__()
        self.page = page
        self.widget = widget
        self.visible = visible
        self.margin = ft.margin.all(0)
        self.bgcolor = ft.Colors.with_opacity(0.05, ft.Colors("brown"))
        self.blur = (12, 12)
        # self.expand = True
        self.image = ft.DecorationImage(
            src=image_theme, fit=ft.ImageFit.COVER, opacity=0.2
        )  # NONE CONTAIN COVER FILL FIT_HEIGHT FIT_WIDTH SCALE_DOWN
        # top_left,top_center,top_right,center_lef,center,center_righ,bottom_left,bottom_right,bottom_center
        self.alignment = ft.alignment.top_center
        self.md_code = md_code
        self.theme_name = "solarized-dark"
        # self.bgcolor = ft.Colors.with_opacity(0.05, ft.Colors("white"))
        # self.bgcolor = "#282828"
        self.bgcolor = ft.Colors.GREY_900
        self.Markdown = ft.Markdown(
            value=self.md_code,
            # scale=0.998,
            # expand=True,
            # expand_loose=True,
            # shrink_wrap=True,
            width=640,
            # height=500,
            # soft_line_break=True,
            fit_content=True,
            opacity=self.opacity_markdown,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,  # COMMON_MARK ,GITHUB_FLAVORED ,GITHUB_WEB
            code_theme=ft.MarkdownCodeTheme.GRUVBOX_DARK,
            code_style_sheet=ft.MarkdownStyleSheet(
                code_text_style=ft.TextStyle(font_family="Roboto Mono"),
            ),
            md_style_sheet=ft.MarkdownStyleSheet(
                code_text_style=ft.TextStyle(font_family="Roboto Mono"),
            ),
        )
        self.alert_visibility = alert_dialog(page=self.page)

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.VerticalAlignment.START,
            spacing=0,
            run_spacing=0,
            scroll="HIDDEN",
            expand=True,
            controls=[
                ft.Container(
                    # left=0,
                    # bottom=0,
                    opacity=self.opacity_markdown,
                    padding=ft.padding.only(left=0, right=0, top=0, bottom=0),
                    height=35,
                    # expand=True,
                    bgcolor="#282828",
                    # bgcolor=ft.Colors.RED,
                    content=self.alert_visibility,
                    alignment=ft.alignment.center,
                ),
                # MARK DOWN EDITOR
                ft.Column(
                    # expand=True,
                    scroll=ft.ScrollMode.ALWAYS,  # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                    controls=[
                        ft.Container(
                            padding=ft.padding.only(left=16, right=0, top=0, bottom=0),
                            expand=True,
                            opacity=self.opacity_markdown,
                            bgcolor="#282828",
                            on_click=lambda widget: self.copy_widget_template(
                                markdown_text=self.Markdown.value
                            ),
                            content=ft.Row(
                                scroll=ft.ScrollMode.ALWAYS,  # ADAPTIVE ,AUTO ,HIDDEN ,ALWAYS
                                controls=[
                                    self.Markdown,
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        )

    def copy_widget_template(self, markdown_text) -> None:
        markdown_text = markdown_text.strip("```python").strip("```")
        self.page.set_clipboard(value=markdown_text)

        self.alert_visibility.visible = False if self.alert_visibility.visible else True
        self.alert_visibility.update()
        time.sleep(0.5)

        self.alert_visibility.visible = False if self.alert_visibility.visible else True
        self.alert_visibility.update()

    def hide_overlay(self):
        self.page.update()

        self.page.overlay.remove(self.widget)
        self.page.update()
