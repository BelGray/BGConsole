# -*- coding: utf-8 -*-
import random
from enums import Color, Param, Tool

class BGC:

    @staticmethod
    def random_color() -> Color:
        """Choose a random color"""
        return random.choice(list(Color))

    @staticmethod
    def random_param() -> Param:
        """Choose a random text parameter"""
        return random.choice(list(Param))

    @staticmethod
    def write(text: str, param: Param = Param.NULL, color: Color = Color.NULL) -> str:
        """Print the stylized text

        :argument text: Text
        :argument param: Text parameter
        :argument color: Text color

        :returns: Stylized text
        """

        print(Tool.OFF.value + str(param.value) + str(color.value) + str(text) + Tool.OFF.value)
        return Tool.OFF.value + str(param.value) + str(color.value) + str(text) + Tool.OFF.value

    @staticmethod
    def scan(label: str = "", label_param: Param = Param.NULL, label_color: Color = Color.NULL, input_text_param: Param = Param.NULL,
             input_text_color: Color = Color.NULL) -> str:
        """Read a string from stylized console input

        :argument label: Text printed before input
        :argument label_param: Label text parameter
        :argument label_color: Label text color
        :argument input_text_param: Input text parameter
        :argument input_text_color: Input text color

        :returns: Input string
        """

        return str(input(Tool.OFF.value + str(label_param.value) + str(label_color.value) + str(label) + Tool.OFF.value + str(input_text_param.value) + str(input_text_color.value)))