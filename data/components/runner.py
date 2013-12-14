import pygame as pg
from .. import setup
from .. import constants as con
from physics import Physics

DIRECT_DICT = {pg.K_LEFT  : (-1),
               pg.K_RIGHT : ( 1)}

class Runner(Physics, pg.sprite.Sprite):
    def __init__(self):
        Physics.__init__(self)
        pg.sprite.Sprite.__init__(self)
        self.width = con.RUNNER_WIDTH
        self.height = con.RUNNER_HEIGHT
        self.right_image = setup.GFX['knightsprite_right']
        self.right_image = pg.transform.scale(self.right_image, (80, 80))
        self.left_image = setup.GFX['knightsprite_left']
        self.left_image = pg.transform.scale(self.left_image, (80, 80))
        self.image = self.right_image
        self.rect = self.image.get_rect()
        self.name = con.RUNNER_NAME
        self.speed = con.RUNNER_SPEED
        self.jump_power = con.JUMP_POWER
        self.fall = False

    def update(self, keys, camera_adjust_x, *args):
        for key in DIRECT_DICT:
            if keys[key]:
                self.rect.x += DIRECT_DICT[key] * self.speed

        if keys[pg.K_SPACE]:
            self.jump()

        if keys[pg.K_RIGHT]:
            self.image = self.right_image
        elif keys[pg.K_LEFT]:
            self.image = self.left_image

        self.rect.right -= camera_adjust_x
        self.rect.y += self.y_vel
        self.physics_update()



    def jump(self):
        if not self.fall:
            self.y_vel = self.jump_power
            self.fall = True



    def collision(self, platforms):
        collided_sprite = pg.sprite.spritecollideany(self, platforms)
        if collided_sprite:
            self.fall = False
            self.rect.bottom = collided_sprite.rect.top
            self.resting_height = self.rect.bottom
        else:
            self.fall = True






