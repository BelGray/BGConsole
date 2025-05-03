from BGConsole.console_text.params.parameters import Reset
from BGConsole.console_text.params.sgr_param import SGRParam


class ConsoleTextStyle:
    """Console text style made with SGR parameters"""

    def __init__(self):
        self.__params = []

    def parameters(self) -> tuple[SGRParam, ...]:
        """Get a list of SGR parameters applied to this style. If there are no applied parameters, returns a tuple with a single Reset parameter.

        :return: SGR parameters list
        """
        return tuple(self.__params) if len(self.__params) > 0 else [Reset()]

    def reset_style(self):
        """Remove all applied SGR parameters"""
        self.__params = []

    def add_parameter(self, param: SGRParam):
        """Apply the SGR parameter"""
        assert isinstance(param, SGRParam)
        self.__params.append(param)
        return self

