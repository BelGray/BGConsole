import re

from BGConsole.console_text.ansi import ANSI
from BGConsole.console_text.params.parameters import Reset
from BGConsole.console_text.text_style import ConsoleTextStyle


class StylizedTextBuilder:
    """Stylized text builder. ANSI sequences are used to stylize console text.

    ANSI support varies across terminals and OS. Verify compatibility before use.
    """

    __ansi = ANSI('\x1b')

    def __init__(self, default_style: ConsoleTextStyle = ConsoleTextStyle()):
        """
        :param default_style: Style applied to text fragments by default. Normal style by default
        """
        self.__reset = StylizedTextBuilder.__ansi.build_sgr_sequence([Reset()])
        self.__default_style = default_style
        self.__stylized_text = ""

    @property
    def default_style(self) -> ConsoleTextStyle:
        return self.__default_style

    @default_style.setter
    def default_style(self, value: ConsoleTextStyle):
        assert isinstance(value, ConsoleTextStyle)
        self.__default_style = value

    def set_text(self, text: str, style: ConsoleTextStyle = None):
        """
        Set new stylized text

        :param text: New text
        :param style: Text style. If the parameter is None, the default style is applied
        """
        if style is None:
            style = self.default_style
        assert isinstance(style, ConsoleTextStyle)
        self.__stylized_text = StylizedTextBuilder.__ansi.build_sgr_sequence(style.parameters()) + str(text) + self.__reset

    def get_text(self, stylized: bool = True) -> str:
        """
        Get the current text

        :param stylized: Returns stylized text if the parameter is True. If False - returns plain unformatted text. Defaults to True
        :return: Stylized text / Plain text
        """
        if stylized:
            return self.__stylized_text
        return re.sub(StylizedTextBuilder.__ansi.sgr_regex, "", self.__stylized_text)

    def clear_text(self):
        """Reset current text"""
        self.__stylized_text = StylizedTextBuilder.__ansi.build_sgr_sequence(self.__default_style.parameters()) + "" + self.__reset

    def add_text_fragment(self, text: str, style: ConsoleTextStyle = None):
        """
        Concatenate stylized text fragment to the current text

        :param text: Text
        :param style: Text style. If the parameter is None, the default style is applied
        """
        if style is None:
            style = self.default_style
        assert isinstance(style, ConsoleTextStyle)
        self.__stylized_text += StylizedTextBuilder.__ansi.build_sgr_sequence(style.parameters()) + str(text) + self.__reset

    def set_default_style(self, style: ConsoleTextStyle):
        """Set new default style. Default style is the style applied to text fragments by default.

        :param style: New default style
        """
        self.default_style = style

    def __str__(self):
        return str(self.__stylized_text)