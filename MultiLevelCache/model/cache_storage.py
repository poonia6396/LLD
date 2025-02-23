from abc import ABC, abstractmethod
from exceptions import StorageFullError

class CacheStorage(ABC):

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def evict(self, key):
        pass

 
class InMemoryCacheStorage(CacheStorage):

    def __init__(self, capacity):
        self.__map = {}
        self.__capacity = capacity
    
    def get(self, key):
        return self.__map.get(key)
    
    def set(self, key, value):
        if self.is_storage_full():
            raise StorageFullError()
        self.__map[key] = value
    
    def evict(self, key):
        return self.__map.remove(key)
    
    def is_storage_full(self) -> bool:
        return len(self.__map) == self.__capacity
    