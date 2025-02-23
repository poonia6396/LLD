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

    def get(self, key) -> ReadResponse:
        value = self.__cache_provider.get(key)
        response_time = self.__level_cache_data.get_read_time()

        if value is None:
            read_response = self.__next.get(key)
            response_time += read_response.get_response_time()

            if read_response.get_value():
                self.__cache_provider.set(key, read_response.get_value())
                response_time += self.__level_cache_data.get_write_time()
        
        return ReadResponse(value, response_time)
    

    def set(self, key, value) -> WriteResponse:
        set_value = self.__cache_provider.get(key)
        response_time = self.__level_cache_data.get_read_time()

        if not set_value or set_value != value:
            self.__cache_provider.set(key, value)
            response_time += self.__level_cache_data.get_write_time()
            response_time += self.__next.set(key, value).get_response_time()
        
        return WriteResponse(response_time)


class NullEffectLevelCache(LevelCache):

    def __init__(self):
        pass

    def get(self, key) -> ReadResponse:
        return ReadResponse(None, 0)
    
    def set(self, key, value) -> WriteResponse:
        return WriteResponse(0)