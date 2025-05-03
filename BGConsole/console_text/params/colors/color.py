class Color:
    """Console color"""
    def __init__(self, color_code: int):
        """
        :param color_code: SGR color code (from 0 to 8)
        """
        self.__color_code: int = int(color_code)

    @property
    def color_code(self) -> int:
        return self.__color_code

    def __str__(self):
        return str(self.color_code)