from enum import Enum
import itertools

class Jump:
    id_iter = itertools.count()
    def __init__(self, start, end):
        self.id = next(self.id_iter)
        self.start = start
        self.end = end

class JumpType(Enum):
    SNAKE = 1
    LADDER = 2