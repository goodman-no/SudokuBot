import pygame as pg

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Square:
    def __init__(self, pos, grid_pos, size):
        self.rendering_pos = pos
        self.grid_pos = grid_pos
        self.size = size
        self.number = None
    
    def set_number(self, n):
        self.number = n
    
    def draw_square(self, WIN):
        pass

class Sudoku:
    def __init__(self, pos, square_size = 20):
        self.pos = pos
        self.square_size = square_size
        self.squares = []

        for y in range(9):
            row = []
            for x in range(9):
                row.append(
                    Square(
                        Position((x * self.square_size) + self.pos.x, 
                                 (y * self.square_size) + self.pos.y), 
                        Position(x, y), self.square_size))
            self.squares.append(row)
    
    def draw_puzzle(self, WIN):
        for row in self.squares:
            for square in row:
                square.draw_square(WIN)

    def solve_puzzle(self):
        pass

    def get_row(self, square):
        return self.squares[square.grid_pos.y]

    def get_column(self, square):
        return [self.squares[i][square.grid_pos.x] for i in range(9)]

    def get_box(self, square):
        pass

    def set_number(self, grid_pos, n):
        self.squares[grid_pos.x][grid_pos.y].set_number(n)

puz = Sudoku(Position(0, 0))