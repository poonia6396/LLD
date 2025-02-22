from typing import List

from model.movie import Movie
from exceptions import NotFoundError, AlreadyExistError

class MovieService:

    def __init__(self):
        self.__movies = {}
    
    def get_movie(self, name: str):
        if name not in self.__movies:
            raise NotFoundError(msg="Movie not found")
        
        return self.__movies.get(name)

    def create_movie(self, name: str):
        if name in self.__movies:
            raise AlreadyExistError(msg="Movie already exists")
        
        movie = Movie(name)
        self.__movies[name] = movie
        return movie