from BGConsole.console_text.colors.color import Color
from .sgr_param import SGRParam

class BoldText(SGRParam):
    """Bold text"""

    def __init__(self):
        super().__init__(1)


class UnderlinedText(SGRParam):
    """Underlined text"""

    def __init__(self):
        super().__init__(4)


class BlinkingText(SGRParam):
    """Blinking text (less than 150 times per minute)"""

    def __init__(self):
        super().__init__(5)


class Negative(SGRParam):
    """Negative display. Inverts the background and text colors."""

    def __init__(self):
        super().__init__(7)


class TextColor(SGRParam):
    """Text color"""

    def __init__(self, color: Color):
        self.__color = color
        super().__init__(30 + color.color_code)

    @property
    def color(self) -> Color:
        return self.__color

    def __str__(self):
        return f"3{self.color}"


class TextBackgroundColor(SGRParam):
    """Text background color"""

    def __init__(self, color: Color):
        self.__color = color
        super().__init__(40 + color.color_code)

    @property
    def color(self) -> Color:
        return self.__color

    def __str__(self):
        return f"4{self.color}"


class FramedText(SGRParam):
    """Framed text"""

    def __init__(self):
        super().__init__(51)


class SurroundedText(SGRParam):
    """Surrounded text"""

    def __init__(self):
        super().__init__(52)


class CrossedOutText(SGRParam):
    """Crossed-out text"""

    def __init__(self):
        super().__init__(53)


class Reset(SGRParam):
    """Disable all attributes (other parameters will be ignored)"""
    
    def __init__(self):
        super().__init__(0)