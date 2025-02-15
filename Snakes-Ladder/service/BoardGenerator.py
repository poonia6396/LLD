from abc import ABC, abstractmethod
import random

from model.jump import Jump, JumpType
from model.board import Board
from .BoardPrinter import BasicBoardPrinter

class BoardGenerator(ABC):

    @abstractmethod
    def generate_board(self, num_of_snakes, num_of_ladders, board_dimensions):
        pass


class BasicBoardGenerator(BoardGenerator):

    def __init__(self):
        self.snake_starts = set()
        self.snake_ends = set()
        self.ladder_starts = set()
        self.ladder_ends = set()

    def generate_random_start_end(self, start_limit, end_limit, set):
        num = 0
        while True:
            num = random.randint(start_limit,end_limit)
            if num not in set:
                set.add(num)
                break
        return num
    
    def generate_snake(self, limit):
        start = self.generate_random_start_end(2, limit, self.snake_starts)
        end = self.generate_random_start_end(1, start-1, self.snake_ends)
        return Jump(start, end)
    
    def generate_ladder(self, limit):
        start = self.generate_random_start_end(1, limit-1, self.ladder_starts)
        while start in self.snake_starts:
            start = self.generate_random_start_end(1, limit-1, self.ladder_starts)
        end = self.generate_random_start_end(start+1, limit, self.ladder_ends)
        return Jump(start, end)

    def generate_jump_objects(self, num_of_objects, jump_type):

        dimension = self.board.dimension
        limit = (dimension*dimension) - 1
        for i in range(num_of_objects):
            if jump_type == JumpType.SNAKE:
                jump_obj = self.generate_snake(limit)
            elif jump_type == JumpType.LADDER:
                jump_obj = self.generate_ladder(limit)

            start_row = int((jump_obj.start-1)/dimension)
            start_col = jump_obj.start%dimension - 1
            self.board.cells[start_row][start_col].jump = jump_obj

    def generate_board(self, num_of_snakes, num_of_ladders, board_dimensions):
        
        self.board = Board(board_dimensions,BasicBoardPrinter())

        self.generate_jump_objects(num_of_snakes,JumpType.SNAKE)
        self.generate_jump_objects(num_of_ladders,JumpType.LADDER)

        return self.board