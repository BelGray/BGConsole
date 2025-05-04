from .console_text import ConsoleTextStyle, ANSI


class Console:
    """Console features"""

    __ansi = ANSI('\x1b')

    @staticmethod
    def stylized_input(prompt: str = "", prompt_style: ConsoleTextStyle = ConsoleTextStyle(), input_text_style: ConsoleTextStyle = ConsoleTextStyle()) -> str:
        """Read a string from stylized console input

        :argument prompt: Text printed before input
        :argument prompt_style: Prompt text style. Normal text by default
        :argument input_text_style: Input text style. Normal text by default

        :returns: Input string
        """

        return str(input(Console.__ansi.build_sgr_sequence(prompt_style.parameters()) + str(prompt) + Console.__ansi.build_sgr_sequence(input_text_style.parameters())))