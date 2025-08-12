class ModelDataView:
    def __init__(
        self, code: dict = dict(), class_oob: dict = dict(), module_os: dict = dict()
    ):
        self.code: dict = code
        self.class_oob: dict = class_oob
        self.module_os: dict = module_os
