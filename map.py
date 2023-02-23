import pygame as pg

mini_map = [
[1,1,1,1,1],
[1,1,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,1,1,1,1]]

import numpy as np

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map() # method to get world map

    # 
    def get_map(self):
        # Number of rows. Here checks number of elems (i.e. lists) in the list
        map_ylen, map_xlen = np.shape(self.mini_map)
        print("map_ylen {}".format(map_ylen))
        print("map_xlen {}".format(map_xlen))
        for j in range(map_ylen):
            row = self.mini_map[j]
            for i in range(map_xlen):
                value = row[i]
                if value:
                    self.world_map[(i, j)] = value


    def draw(self):
        # iterate over list of lists
        # each list corresponds to a row in the 2D map
        for pos in self.world_map:
            #print(pos)
            x_tl_rect = pos[0] * 100
            y_tl_rect = pos[1] * 100
            width_rect = 100
            height_rect = 100
            pg.draw.rect(self.game.screen, 'red', pg.Rect(x_tl_rect, y_tl_rect, width_rect, height_rect), 2)