from abc import ABC, abstractmethod

class Subscriber(ABC):

    @abstractmethod
    def consume(message):
        pass