__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import constants

class Ground(pg.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pg.sprite.Sprite.__init__(self)
        self.width = constants.GROUND_WIDTH
        self.height = constants.GROUND_HEIGHT
        self.image = pg.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = constants.FOREST_GREEN
        self.name = 'ground'

    def update(self, keys, camera_adjust_x, *args):
        self.rect.right -= camera_adjust_x
        self.image.fill(self.color)





