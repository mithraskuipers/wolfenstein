import pygame as pg
import sys
from settings import *
from map import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)

    def update(self):
        pg.display.flip() # update full display surface
        # clock.tick() this method should be called once per frame. It will compute how many . milliseconds have passed since the previous call.
        # clock.tick(60) for every second AT MOST 60 frames should pass
        self.delta_time = self.clock.tick(FPS) # for every second at most FPS frames should pass
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")

    def draw(self):
        self.screen.fill("black")
        self.map.draw()
 
    def check_events(self):
        for event in pg.event.get():
            # if shutdown request event  or key physically pressed down and escape key pressed
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit() # closes pygame
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()
