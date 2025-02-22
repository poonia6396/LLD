from typing import List

from model.screen import Screen

class Theatre:

    def __init__(self, screens: List[Screen]):
        self.__screens = screens
        