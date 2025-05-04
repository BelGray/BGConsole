import random

from .color import Color


class RGB(Color):
    """RGB color"""

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        """
        :argument red: Red color channel (from 0 to 255)
        :argument green: Green color channel (from 0 to 255)
        :argument blue: Blue color channel (from 0 to 255)
        """

        assert 0 <= red <= 255
        assert 0 <= green <= 255
        assert 0 <= blue <= 255

        self.__r: int = int(red)
        self.__g: int = int(green)
        self.__b: int = int(blue)

        super().__init__(8)

    @property
    def red(self) -> int:
        return self.__r

    @property
    def green(self) -> int:
        return self.__g

    @property
    def blue(self) -> int:
        return self.__b

    @red.setter
    def red(self, value: int):
        assert 0 <= value <= 255
        self.__r = int(value)

    @green.setter
    def green(self, value: int):
        assert 0 <= value <= 255
        self.__g = int(value)

    @blue.setter
    def blue(self, value: int):
        assert 0 <= value <= 255
        self.__b = int(value)

    def set_random_color(self):
        """Set random RGB color"""
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)

    def set_color(self, red: int = None, green: int = None, blue: int = None):
        """Set RGB color. If the value of a parameter is None, it will not be changed.

        :argument red: Red color channel (from 0 to 255)
        :argument green: Green color channel (from 0 to 255)
        :argument blue: Blue color channel (from 0 to 255)
        """
        if red is not None:
            self.red = red
        if green is not None:
            self.green = green
        if blue is not None:
            self.blue = blue

    def __str__(self):
        return f"{str(self.color_code)};2;{self.red};{self.green};{self.blue}"
