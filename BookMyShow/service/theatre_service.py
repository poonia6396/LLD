from typing import List

from model.theatre import Theatre, Screen, Seat

class TheatreService:

    def __init__(self):
        self.__theatres = []
    
    def create_theatres(self, name: str, city: str):
        theatre = Theatre(name, city)
        self.__theatres.append(theatre)
        return theatre
    
    def create_screen_in_theatre(self, name: str, theatre: Theatre):
        screen = Screen(name, theatre)
        theatre.add_screen(screen)
        return screen
    
    def create_seat_in_screen(self, seat_num: int, screen: Screen):
        seat = Seat(seat_num)
        screen.add_seat(seat)
        return seat