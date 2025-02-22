from abc import ABC, abstractmethod
from typing import List

from model.show import Show
from model.theatre import Seat

class SeatLockProvider(ABC):

    @abstractmethod
    def lock_seats(self, show: Show, seats: List[Seat], user_id: int):
        pass

    @abstractmethod
    def validate_lock(self, show_id: int, seat: Seat, user_id: int) -> bool:
        pass
    
    @abstractmethod
    def unlock_seats(self, show: Show, seats: List[Seat]):
        pass
    
    @abstractmethod
    def get_locked_seat_nums(self, show: Show):
        pass