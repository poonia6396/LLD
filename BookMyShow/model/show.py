from movie import Movie
from typing import List

from model.seat import Seat

class Show:

    def __init__(self, movie: Movie, seats: List[Seat], start_time, end_time):
        self.__movie = movie
        self.__start_time = start_time
        self.__end_time = end_time
        self.__seats = seats