from typing import List

from model.level_cache import LevelCache
from model.response import ReadResponse, WriteResponse


class CacheService:

    def __init__(self, multi_level_cache: LevelCache, avg_count):
        self.__multi_level_cache = multi_level_cache
        self.__avg_count = avg_count
        self.__read_times = []
        self.__write_times = []

    def set(self, key, value) -> WriteResponse:
        write_response = self.__multi_level_cache.set(key, value)
        self.add_times(write_response.get_response_time(), self.__write_times)
        return write_response

    def get(self, key) -> ReadResponse:
        read_response = self.__multi_level_cache.get(key)
        self.add_times(read_response.get_response_time(), self.__read_times)
        return read_response

    def get_avg_read_time(self):
        return sum(self.__read_times)/self.__avg_count

    def get_avg_write_time(self):
        return sum(self.__write_times)/self.__avg_count
    
    def add_times(self, time, time_list: List[int]):
        time_list.append(time)

        if len(time_list) > self.__avg_count:
            time_list.pop(0)

    
