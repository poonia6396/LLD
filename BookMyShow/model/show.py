import itertools
from typing import List

from model.movie import Movie
from model.theatre import Screen

class Show:
    id_iter = itertools.count()
    def __init__(self, movie: Movie, screen: Screen, start_time, end_time):
        self.__id = next(self.id_iter)
        self.__movie = movie
        self.__start_time = start_time
        self.__end_time = end_time
        self.__screen = screen
    
    def get_id(self):
        return self.__id