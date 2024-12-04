import pygame
import pygame as pg

class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        pg.init()

        window = pg.display.set_mode(size=(800, 640))

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
