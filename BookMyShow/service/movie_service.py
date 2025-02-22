from typing import List

from model.movie import Movie

class MovieService:

    def __init__(self):
        self.__movies = {}
    
    def create_movie(self, name: str):
        if name in self.__movies:
            print("Movie:", name, "already exists")
        movie = Movie(name)
        self.__movies[name] = movie
        return movie