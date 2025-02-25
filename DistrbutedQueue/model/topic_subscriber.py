from threading import Lock
from .subsriber import Subscriber

class TopicSubscriber:

    def __init__(self, subscriber: Subscriber):
        self.__subscriber = subscriber
        self.__offset = 0
        self.__lock = Lock()

    def get_lock(self):
        return self.__lock
    
    def get_subscriber(self):
        return self.__subscriber

    def get_offset(self):
        return self.__offset
    
    def reset_offset(self):
        with self.__lock:
            self.__offset = 0

    def increment_offset(self):
        with self.__lock:
            self.__offset += 1