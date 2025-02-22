from enum import Enum

class SeatStatus(Enum):
    AVAILABLE, BOOKED = 1, 2

class Seat:

    def __init__(self, number):
        self.__number = number