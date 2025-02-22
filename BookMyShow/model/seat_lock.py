from datetime import datetime, timedelta

class SeatLock:

    def __init__(self, show, seat, user, timeout_in_seconds):
        self.__show = show
        self.__seat = seat
        self.__user = user
        self.__expiry_time = datetime.now() + timedelta(timeout_in_seconds)
    
    def get_user(self):
        return self.__user

    def is_expired(self) -> bool:
        return datetime.now() > self.__expiry_time