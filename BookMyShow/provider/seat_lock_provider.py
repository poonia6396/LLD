from abc import ABC, abstractmethod

class SeatLockProvider(ABC):

    @abstractmethod
    def lock_seat():
        pass