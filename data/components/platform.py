import pygame as pg
from .. import constants


class Platform(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, mover=False):
        pg.sprite.Sprite.__init__(self)
        self.width = constants.PLAT_WIDTH
        self.height = constants.PLAT_HEIGHT
        self.image = pg.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.starty = y
        self.rect.x = x
        self.rect.y = y
        self.color = constants.RED
        self.name = 'platform'
        self.moving_down = True
        self.mover = mover

    def update(self, keys, camera_adjust_x, *args):
        self.rect.right -= camera_adjust_x
        self.image.fill(self.color)
        if self.mover:
            self.move_vertical()

    def move_vertical(self):
        if (self.rect.y < (100 + self.starty)
            and self.moving_down):
            self.rect.y += 1
        elif (self.rect.y >= (100 + self.starty) and self.moving_down):
            self.moving_down = False
            self.rect.y -= 1
        elif (self.moving_down == False and self.rect.y > self.starty):
            self.rect.y -= 1
        else:
            self.moving_down = True
            self.rect.y += 1



