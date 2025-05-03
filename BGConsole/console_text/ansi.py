from typing import Sequence

from BGConsole.console_text.params.sgr_param import SGRParam


class ANSI:
    """ANSI sequences builder.

    ANSI support varies across terminals and OS. Verify compatibility before use.
    """

    def __init__(self, esc_symbol: str):
        """
        Escape symbol (ESC) is a control character in the ASCII table that initiates ANSI escape sequences.

        :param esc_symbol: Escape symbol
        """

        self.__esc = esc_symbol
        self.__csi = f'{esc_symbol}['
        self.__sgr_regex = rf'\{esc_symbol}\[[0-9;]*m'

    @property
    def sgr_regex(self) -> str:
        return self.__sgr_regex

    def build_sgr_sequence(self, sgr: Sequence[SGRParam]) -> str:
        """Build ANSI CSI sequence from SGR parameters

        :argument sgr: Sequence of SGR parameters
        :return: Complete CSI sequence string (e.g. '\x1b[0m')
        """
        return f"{self.__csi}{';'.join(map(str, sgr))}m"