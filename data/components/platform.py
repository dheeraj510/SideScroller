import pygame as pg
from .. import constants


class Platform(pg.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pg.sprite.Sprite.__init__(self)
        self.width = constants.PLAT_WIDTH
        self.height = constants.PLAT_HEIGHT
        self.image = pg.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = constants.RED

    def update(self, keys, camera_adjust_x, *args):
        self.rect.right -= camera_adjust_x
        self.image.fill(self.color)
