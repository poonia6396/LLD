from abc import ABC, abstractmethod

from .response import ReadResponse, WriteResponse
from provider.cache_provider import CacheProvider

class LevelCacheData:

    def __init__(self, read_response_time, write_response_time):
        self.__read_response_time = read_response_time
        self.__write_response_time = write_response_time
    
    def get_read_time(self):
        return self.__read_response_time
    
    def get_write_time(self):
        return self.__write_response_time


class LevelCache(ABC):

    @abstractmethod
    def get(self, key) -> ReadResponse:
        pass
    
    @abstractmethod
    def set(self, key, value) -> WriteResponse:
        pass


class DefaultLevelCache(LevelCache):

    def __init__(self, level_cache_data: LevelCacheData, cache_provider: CacheProvider, next_level_cache: LevelCache):
        self.__level_cache_data = level_cache_data
        self.__cache_provider = cache_provider
        self.__next = next_level_cache

    def get()