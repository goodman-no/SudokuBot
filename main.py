import pygame as pg
from sudoku import Sudoku, Position
import sys

pg.init()

WIDTH, HEIGHT = 600, 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))

puz = Sudoku(Position(120, 120))

running = True
while running:
    events = pg.event.get()

    puz.update_puzzle(events)

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    WIN.fill((0, 0, 0))
    puz.draw_puzzle(WIN)
    pg.display.update()

