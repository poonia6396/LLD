from typing import List
import itertools
from enum import Enum


class SeatStatus(Enum):
    AVAILABLE, BOOKED = 1, 2


class Seat:

    def __init__(self, number, status: SeatStatus):
        self.__number = number
        self.__status = status


class Screen:

    def __init__(self, name, theatre):
        self.__name = name
        self.__seats = []
        self.__theatre = theatre
    
    def add_seat(self, seat: Seat):
        self.__seats.append(seat)
    

class Theatre:
    id_iter = itertools.count()
    def __init__(self, name: str, city: str):
        self.__id = next(self.id_iter)
        self.__name = name
        self.__city = city
        self.__screens = []
    
    def add_screen(self, screen: Screen):
        self.__screens.append(screen)
        