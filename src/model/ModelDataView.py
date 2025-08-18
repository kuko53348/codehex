class ModelDataView:
    def __init__(
        self, code: dict = dict(), class_obb: dict = dict(), module_os: dict = dict()
    ):
        self.code: dict = code
        self.class_obb: dict = class_obb
        self.module_os: dict = module_os
