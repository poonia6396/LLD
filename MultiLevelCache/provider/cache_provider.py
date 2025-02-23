from model.cache_storage import CacheStorage
from model.eviction_policy import EvictionPolicy

from exceptions import StorageFullError

class CacheProvider:

    def __init__(self, storage: CacheStorage, eviction_policy: EvictionPolicy):
        self.__storage = storage
        self.__eviction_policy = eviction_policy
    
    def set(self, key, value):
        try:
            self.__storage.set(key, value)
            self.__eviction_policy.accessed_key(key)
        except StorageFullError as e:
            key_to_evict = self.__eviction_policy.get_eviction_key()
            self.__storage.evict(key_to_evict)
            self.set(key, value)


    def get(self, key):
        value = self.__storage.get(key)
        self.__eviction_policy.accessed_key(key)

        return value