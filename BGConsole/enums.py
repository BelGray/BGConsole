from enum import Enum

class Color(Enum):
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RED = "\033[31m"
    GREEN = '\033[92m'
    MUSTARD = '\033[93m'
    CRIMSON = '\033[91m'
    YELLOW = '\033[33m'
    PURPLE = "\033[35m"
    BLACK = "\033[30m"
    WHITE = "\033[37m"
    NULL = ""

class Param(Enum):
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NULL = ""

class Tool(Enum):
    EMPTY = ""
    OFF = '\033[0m'
    NULL = ""