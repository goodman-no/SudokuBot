import pygame as pg
from sudoku import Sudoku
from util import Position, COLORS
from ui import UI_MANAGER, Button, Text
import sys

pg.init()

WIDTH, HEIGHT = 600, 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))
ui_manager = UI_MANAGER()

puz = Sudoku(Position(120, 120))
sudoku_text = Text(ui_manager, Position(230, 60),
                   "Sudoku Solver",
                   font_color=COLORS.WHITE)
solve_button = Button(ui_manager, Position(350, 525),
                      "SOLVE",
                      puz.solve_puzzle,
                      font_color=COLORS.WHITE)
clear_button = Button(ui_manager, Position(150, 525),
                      "CLEAR",
                      puz.clear_puzzle,
                      font_color=COLORS.WHITE)

running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        puz.update_puzzle(event)
        ui_manager.update(event)

    WIN.fill((0, 0, 0))
    puz.draw_puzzle(WIN)
    ui_manager.draw(WIN)
    pg.display.update()