import itertools
from typing import List
from enum import Enum

from exceptions import InvalidStateError

from model.show import Show
from model.theatre import Seat
from model.user import User

class BookingStatus(Enum):
    CREATED, CONFIRMED, CANCELLED, EXPIRED = 1, 2, 3, 4

class Booking:
    id_iter = itertools.count()
    def __init__(self, show: Show, seats: List[Seat], user: User):
        self.__id = next(self.id_iter)
        self.__show = show
        self.__seats = seats
        self.__user = user
        self.__status = BookingStatus.CREATED
    
    def is_confirmed(self) -> bool:
        return self.__status == BookingStatus.CONFIRMED
    
    def get_id(self):
        return self.__id

    def get_show(self) -> Show:
        return self.__show

    def get_seats(self) -> List[Seat]:
        return self.__seats
    
    def get_user(self) -> User:
        return self.__user
    
    def confirm_booking(self):
        if self.__status != BookingStatus.CREATED:
            raise InvalidStateError()
        
        self.__status == BookingStatus.CONFIRMED
    
    def cancel_booking(self):
        if self.__status != BookingStatus.CREATED or self.__status != BookingStatus.CONFIRMED:
            raise InvalidStateError()
        
        self.__status == BookingStatus.CANCELLED
    
    def expire_booking(self):
        if self.__status != BookingStatus.CREATED:
            raise InvalidStateError()

        self.__status == BookingStatus.EXPIRED

