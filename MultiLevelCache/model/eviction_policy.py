from abc import ABC, abstractmethod
from collections import deque

class EvictionPolicy(ABC):

    @abstractmethod
    def accessed_key(self, key):
        pass

    @abstractmethod
    def get_eviction_key(self) -> object:
        pass

class LRUEvictionPolicy(EvictionPolicy):

    def __init__(self):
        self.__dll = deque()
        self.__set = set()
    
    def accessed_key(self, key):
        if key in self.__set:
            self.__dll.remove(key)

        self.__set.add(key) 
        self.__dll.append(key)
    
    def get_eviction_key(self):
        key = self.__dll.popleft()
        self.__set.remove(key)
        return key
