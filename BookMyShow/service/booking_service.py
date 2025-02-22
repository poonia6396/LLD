from typing import List

from exceptions import SeatAlreadyBookedError

from provider.seat_lock_provider import SeatLockProvider

from model.booking import Booking
from model.show import Show
from model.user import User
from model.theatre import Seat

class BookingService:

    def __init__(self, seat_lock_provider: SeatLockProvider):
        self.__bookings: List[Booking] = []
        self.__seat_lock_provider = seat_lock_provider

    def get_all_confirmed_bookings_of_show(self, show: Show) -> List[Booking]:
        result = []
        for booking in self.__bookings:
            if booking.is_confirmed() and booking.get_show().get_id() == show.get_id():
                result.append(booking)
        
        return result

    def get_booked_seat_ids_of_show(self, show: Show) -> List[int]:
        result = []
        confirmed_bookings_of_show = self.get_all_confirmed_bookings_of_show(show)
        for confirmed_booking in confirmed_bookings_of_show:
            booking_seats = confirmed_booking.get_seats()
            result.extend([seat.get_number() for seat in booking_seats])
        
        return result

    def create_booking(self, user: User, show: Show, seats: List[Seat]) -> Booking:
        if not self.all_seats_are_available(show, seats):
            raise SeatAlreadyBookedError()
        
        self.__seat_lock_provider.lock_seats(show, seats, user)
        booking = Booking(show, seats, user)
        self.__bookings.append(booking)
        return booking

    def confirm_booking(self, booking: Booking) -> Booking:
        booking_seats = booking.get_seats()
        booking_show = booking.get_show()
        booking_user = booking.get_user()
        for seat in booking_seats:
            if not self.seat_lock_provider.validate_lock(booking_show, seat, booking_user):
                raise PermissionError()
        booking.confirm_booking()
        return booking

    def all_seats_are_available(self, show: Show, seats: List[Seat]):
        booked_seats_ids = self.get_booked_seat_ids_of_show(show)
        for seat in seats:
            if seat.get_number() in booked_seats_ids:
                return False
        
        return True
        
