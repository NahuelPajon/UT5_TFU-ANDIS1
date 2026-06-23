class ViewModelError(Exception):
    def __init__(self, detail: str):
        super().__init__(detail)
        self.detail = detail


class ResourceNotFoundError(ViewModelError):
    pass


class BusinessRuleError(ViewModelError):
    pass

