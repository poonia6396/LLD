from service.booking_service import BookingService

from provider.seat_lock_provider import SeatLockProvider

from model.show import Show

class SeatAvailibilityService:

    def __init__(self, booking_service: BookingService, seat_lock_provider: SeatLockProvider):
        self.__booking_service = booking_service
        self.__seat_lock_provider = seat_lock_provider
    
    def get_available_seats(self, show: Show):
        pass