class ModelDataView:
    def __init__(
        self, code: dict = dict(), class_code: dict = dict(), os_code: dict = dict()
    ):
        self.code: dict = code
        self.class_code: dict = class_code
        self.os_code: dict = os_code
