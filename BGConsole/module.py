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
    def write(text: str, param: Param = None, color: Color = None):
        if param == None:
            param = Param.NULL
        if color == None:
            color = Color.NULL

        print(Tool.OFF.value + str(param.value) + str(color.value) + str(text) + Tool.OFF.value)
        return Tool.OFF.value + str(param.value) + str(color.value) + str(text) + Tool.OFF.value

    @staticmethod
    def scan(label: str, label_param: Param = None, label_color: Color = None, input_text_param: Param = None,
             input_text_color: Color = None):
        if label == None:
            label = ""
        if label_color == None:
            label_color = Color.NULL
        if input_text_color == None:
            input_text_color = Color.NULL
        if label_param == None:
            label_param = Param.NULL
        if input_text_param == None:
            input_text_param = Param.NULL

        return str(input(Tool.OFF.value + str(label_param.value) + str(label_color.value) + str(label) + Tool.OFF.value + str(input_text_param.value) + str(input_text_color.value)))