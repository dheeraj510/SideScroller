__author__ = 'justinarmstrong'

import pygame as pg
from .. import constants as con

class Coin(pg.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pg.sprite.Sprite.__init__(self)
        self.color = con.GOLD
        self.width = con.COIN_WIDTH
        self.height = con.COIN_HEIGHT
        self.color = con.GOLD
        self.image = pg.Surface((self.width,
                                 self.height)).convert()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = 'coin'

    def update(self, keys, camera_adjust_x, *args):
        self.rect.x -= camera_adjust_x
        self.image.fill(self.color)




