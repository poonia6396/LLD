from movie import Movie
from typing import List

from model.theatre import Screen

class Show:

    def __init__(self, movie: Movie, screen: Screen, start_time, end_time):
        self.__movie = movie
        self.__start_time = start_time
        self.__end_time = end_time
        self.__screen = screen