import pygame as pg
from util import Position, COLORS

class UI_MANAGER:
    def __init__(self):
        self.elements = []
    
    def draw(self, WIN):
        for element in self.elements:
            element.draw(WIN)
    
    def update(self, event):
        for element in self.elements:
            element.update(event)

class UI:
    def __init__(self, MANAGER, pos, size):
        MANAGER.elements.append(self)
        self.pos = pos
        self.size = size
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)
    
    def draw(self, WIN):
        pass

    def update(self, events):
        pass

class Text(UI):
    def __init__(self, MANAGER, pos, text, font_size=36, font=None, font_color=COLORS.BLACK):
        self.text = text
        self.font = pg.font.SysFont(font, font_size)
        self.img = self.font.render(self.text, True, font_color)

        super().__init__(MANAGER, pos, Position(self.img.get_width(), self.img.get_height()))
    
    def draw(self, WIN):
        WIN.blit(self.img, (self.pos.x, self.pos.y))

class Button(Text):
    def __init__(self, MANAGER, pos, text, func, font_size=36, font=None, font_color=COLORS.BLACK):
        super().__init__(MANAGER, pos, text, font_size, font, font_color)
        self.func = func
    
    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(pg.mouse.get_pos()):
            self.func()