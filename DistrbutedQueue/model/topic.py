import itertools
from typing import List

from .topic_subscriber import TopicSubscriber

class Topic:

    id_iter = itertools.count()
    def __init__(self, name):
        self.__id = next(self.id_iter)
        self.__name = name
        self.__messages = []
        self.__topic_subscribers: List[TopicSubscriber] = []
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_topic_subscribers(self):
        return self.__topic_subscribers
    
    def get_messages(self):
        return self.__messages
    
    def add_message(self, message):
        self.__messages.append(message)