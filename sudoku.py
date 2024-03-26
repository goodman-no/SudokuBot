import pygame as pg
from util import Position, COLORS

class Square:
    def __init__(self, pos, grid_pos, size):
        self.rendering_pos = pos
        self.grid_pos = grid_pos
        self.size = size
        self.rect = pg.Rect(self.rendering_pos.x, self.rendering_pos.y, self.size, self.size)

        self.font = pg.font.SysFont(None, 36)
        self.num_img = None

        self.number = None

        self.indexing_number = None
    
    def set_number(self, n):
        self.number = n

        if n != None:
            self.num_img = self.font.render(str(self.number), True, COLORS.BLACK)
        else:
            self.num_img = None
    
    def set_possibility(self, possible):
        if self.number != None:
            if possible:
                self.num_img = self.font.render(str(self.number), True, COLORS.BLACK)
            else:
                self.num_img = self.font.render(str(self.number), True, COLORS.RED)
    
    def draw_square(self, WIN):
        pg.draw.rect(WIN, COLORS.WHITE, self.rect)
        pg.draw.rect(WIN, COLORS.BLACK, self.rect, width=1)

        if self.num_img != None:
            WIN.blit(self.num_img, (self.rendering_pos.x + (self.size / 3), self.rendering_pos.y + (self.size / 3)))

class Sudoku:
    def __init__(self, pos, square_size = 40):
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
        
        self.selected_square = self.squares[0][0]
    
    def draw_puzzle(self, WIN):
        for row in self.squares:
            for square in row:
                square.draw_square(WIN)
        
        for x in range(3):
            for y in range(3):
                size = self.square_size * 3
                box_border = pg.Rect(self.pos.x + (x * size), self.pos.y + (y * size), size, size)
                pg.draw.rect(WIN, (0, 0, 0), box_border, width=3)

    def update_puzzle(self, event):
        
        if event.type == pg.KEYDOWN:
            if event.key in [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9]:
                self.selected_square.set_number(int(pg.key.name(event.key)))
            if event.key in [pg.K_0]:
                self.selected_square.set_number(None)
        elif event.type == pg.MOUSEBUTTONDOWN:
            for row in self.squares:
                for square in row:
                    if square.rect.collidepoint(pg.mouse.get_pos()):
                        self.selected_square = square

        for row in self.squares:
            for square in row:
                square.set_possibility(self.is_possible(square))

    def solve_puzzle(self):
        empty_squares = []

        for row in self.squares:
            for square in row:
                if square.number == None:
                    empty_squares.append(square)

        backtrack_i = 0
        while backtrack_i < len(empty_squares):

            if empty_squares[backtrack_i].indexing_number == None:
                empty_squares[backtrack_i].indexing_number = 1
            else:
                empty_squares[backtrack_i].indexing_number += 1
            
            if empty_squares[backtrack_i].indexing_number > 9:
                if backtrack_i == 0:
                    print(f"PUZZLE IMPOSSIBLE")
                    break
                else:
                    s = empty_squares[backtrack_i]
                    s.indexing_number = None
                    self.squares[s.grid_pos.y][s.grid_pos.x].set_number(None)
                    backtrack_i -= 1
            else:
                s = empty_squares[backtrack_i]
                self.squares[s.grid_pos.y][s.grid_pos.x].set_number(empty_squares[backtrack_i].indexing_number)
                print(f"{backtrack_i} : POSSIBLE? : {self.is_possible(self.squares[s.grid_pos.y][s.grid_pos.x])}")
                if self.is_possible(self.squares[s.grid_pos.y][s.grid_pos.x]):
                    backtrack_i += 1
                    

    def get_row(self, square):
        return [s.number for s in self.squares[square.grid_pos.y]]

    def get_column(self, square):
        return [s.number for s in [self.squares[i][square.grid_pos.x] for i in range(9)]]

    def get_box(self, square):
        box_x = 0
        box_y = 0


        if square.grid_pos.x < 3:
            box_x = 0
        elif square.grid_pos.x < 6:
            box_x = 3
        elif square.grid_pos.x < 9:
            box_x = 6
        
        if square.grid_pos.y < 3:
            box_y = 0
        elif square.grid_pos.y < 6:
            box_y = 3
        elif square.grid_pos.y < 9:
            box_y = 6

        box = []

        for x in range(3):
            for y in range(3):
                box.append(self.squares[box_y + y][box_x + x])

        return [s.number for s in box]
    
    def is_possible(self, square):
        if square.number == None:
            return None
        
        return not (self.appears_twice(self.get_row(square), square.number) or 
                    self.appears_twice(self.get_column(square), square.number) or
                    self.appears_twice(self.get_box(square), square.number))
    
    def group_is_possible(self, squares):
        for square in squares:
            if not self.is_possible(square):
                return False
        
        return True
    
    @staticmethod 
    def appears_twice(list, item):
        count = 0

        for element in list:
            if element == item:
                count += 1
        
        return count >= 2