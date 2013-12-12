import pygame as pg
from .. import setup
from .. import constants

DIRECT_DICT = {pg.K_LEFT  : (-1),
               pg.K_RIGHT : ( 1)}

class Runner(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.width = constants.RUNNER_WIDTH
        self.height = constants.RUNNER_HEIGHT
        self.right_image = setup.GFX['knightsprite_right']
        self.right_image = pg.transform.scale(self.right_image, (80, 80))
        self.left_image = setup.GFX['knightsprite_left']
        self.left_image = pg.transform.scale(self.left_image, (80, 80))
        self.image = self.right_image
        self.rect = self.image.get_rect()
        self.name = constants.RUNNER_NAME
        self.speed = constants.RUNNER_SPEED
        self.resting_height = constants.STARTY
        self.jump = False
        self.fall = False

    def update(self, keys, camera_adjust_x, *args):
        for key in DIRECT_DICT:
            if keys[key]:
                self.rect.x += DIRECT_DICT[key] * self.speed

        if keys[pg.K_SPACE] and self.fall == False:
            self.jump = True

        if keys[pg.K_RIGHT]:
            self.image = self.right_image
        elif keys[pg.K_LEFT]:
            self.image = self.left_image

        self.rect.right -= camera_adjust_x
        self.vertical_move()



    def vertical_move(self):
        if self.jump:
            self.rect.y -= constants.JUMP_SPEED
            if self.rect.bottom <= self.resting_height - constants.MAX_HEIGHT:
                self.jump = False
                self.fall = True
        elif self.fall:
            self.rect.y += constants.FALL_SPEED

        else:
            self.rect.bottom = self.resting_height


    def collision(self, platforms):
        collided_sprite = pg.sprite.spritecollideany(self, platforms)
        if collided_sprite:
            self.fall = False
            self.rect.bottom = collided_sprite.rect.top
            self.resting_height = self.rect.bottom






