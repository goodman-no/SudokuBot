import pygame as pg
from sudoku import Sudoku
from util import Position, COLORS
from ui import Button
import sys

pg.init()

WIDTH, HEIGHT = 600, 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))

puz = Sudoku(Position(120, 120))
solve_button = Button(Position(275, 525),
                      "SOLVE",
                      puz.solve_puzzle,
                      font_color=COLORS.WHITE)

running = True
while running:
    events = pg.event.get()


    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        puz.update_puzzle(event)
        solve_button.update(event)

    WIN.fill((0, 0, 0))
    puz.draw_puzzle(WIN)
    solve_button.draw(WIN)
    pg.display.update()

