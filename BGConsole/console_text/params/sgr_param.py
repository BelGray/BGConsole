class SGRParam:
    """Select Graphic Rendition parameter"""

    def __init__(self, code: int):
        """
        :param code: SGR parameter code
        """
        self.__code = code

    @property
    def code(self) -> int:
        return self.__code

    def __str__(self):
        return str(self.code)