class FlutterModelView:
    def __init__(
        self,
        flutter_class: dict = dict(),
        flutter_async: dict = dict(),
        flutter_ui: dict = dict(),
        flutter_state: dict = dict(),
        flutter_navigation: dict = dict(),
        flutter_effects: dict = dict(),
        flutter_lists: dict = dict(),
        flutter_inputs: dict = dict(),
        flutter_api: dict = dict(),
        flutter_utilities: dict = dict(),
    ):
        self.flutter_class: dict = flutter_class
        self.flutter_async: dict = flutter_async
        self.flutter_ui: dict = flutter_ui
        self.flutter_state: dict = flutter_state
        self.flutter_navigation: dict = flutter_navigation
        self.flutter_effects: dict = flutter_effects
        self.flutter_lists: dict = flutter_lists
        self.flutter_inputs: dict = flutter_inputs
        self.flutter_api: dict = flutter_api
        self.flutter_utilities: dict = flutter_utilities
