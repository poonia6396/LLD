import itertools
from typing import List
from enum import Enum

from model.show import Show
from model.seat import Seat
from model.user import User

class BookingStatus(Enum):
    CREATED, CONFIRMED, CANCELLED = 1, 2, 3

class Booking:
    id_iter = itertools.count()
    def __init__(self, show: Show, seats: List[Seat], user: User):
        self.__id = next(self.id_iter)
        self.__show = show
        self.__seats = seats
        self.__user = user
        self.__status = BookingStatus.CREATED

