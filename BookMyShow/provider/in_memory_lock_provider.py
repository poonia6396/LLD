
from typing import List
from threading import Lock
from .seat_lock_provider import SeatLockProvider

from model.theatre import Seat
from model.seat_lock import SeatLock
from model.show import Show
from model.user import User

class InMemorySeatLockProvider(SeatLockProvider):
    
    def __init__(self, timeout):
        self.__lock_seat_map = {}
        self.__lock_timeout = timeout
        self.__lock = Lock()
    

    def is_seat_locked(self, show: Show, seat: Seat) -> bool:
        return show.get_id() in self.__lock_seat_map and seat.get_number() in self.__lock_seat_map[show.get_id()]


    def unlock_seat(self, show: Show, seat: Seat):
        if self.is_seat_locked(show, seat):
            self.__lock_seat_map[show.get_id()].remove(seat.get_number())


    def lock_seat(self, show: Show, seat: Seat, user: User):
        if show.get_id() not in self.__lock_seat_map:
            self.__lock_seat_map[show.get_id()] = {}
        
        self.__lock_seat_map[show.get_id()][seat.get_number()] = SeatLock(show, seat, user, self.__lock_timeout)


    def lock_seats(self, show: Show, seats: List[Seat], user: User):
        with self.__lock:
            for seat in seats:
                if self.is_seat_locked(show, seat):
                    raise PermissionError()

            for seat in seats:
                self.lock_seat(show, seat, user)

    
    def validate_lock(self, show: Show, seat: Seat, user: User) -> bool:
        return self.is_seat_locked(show, seat) and self.__lock_seat_map[show.get_id()][seat.get_number()].get_user().get_id() == user.get_id()
    
    
    def unlock_seats(self, show: Show, seats: List[Seat], user: User):
        for seat in seats:
            if self.validate_lock(show, seat, user):
                self.unlock_seat(show, seat)
    
    def get_locked_seats_nums(self, show: Show) -> List[int]:
        result = []
        if show.get_id() in self.__lock_seat_map:
            result = list(self.__lock_seat_map.keys())

        return result