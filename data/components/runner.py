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
        self.right_image = pg.transform.scale(self.right_image, (80, 80)).convert_alpha()
        self.left_image = setup.GFX['knightsprite_left']
        self.left_image = pg.transform.scale(self.left_image, (80, 80)).convert_alpha()
        self.image = self.right_image
        self.rect = self.image.get_rect()
        self.rect.width *= .75
        self.name = con.RUNNER_NAME
        self.speed = con.RUNNER_SPEED
        self.jump_power = con.JUMP_POWER
        self.moving_right = True
        self.ok_to_jump = True
        self.dead = False


    def update(self, keys, camera_adjust_x, *args):
        ground_and_platforms = args[0]

        self.event_loop(keys)
        self.check_x_collisions(ground_and_platforms)
        self.rect.y += self.y_vel
        self.check_y_collisions(ground_and_platforms)
        self.physics_update()
        self.adjust_camera(camera_adjust_x)


    def check_x_collisions(self, colliders):
        obstacle = pg.sprite.spritecollideany(self, colliders)

        if self.moving_right and obstacle:
            self.rect.right = obstacle.rect.left
        elif not self.moving_right and obstacle:
            self.rect.left = obstacle.rect.right


    def check_y_collisions(self, colliders):
        obstacle = pg.sprite.spritecollideany(self, colliders)

        if self.y_vel < 0 and obstacle:
            self.rect.top = obstacle.rect.bottom
            self.y_vel = 0
        elif self.y_vel > 0 and obstacle:
            self.rect.bottom = obstacle.rect.top
            self.y_vel = 0
            self.ok_to_jump = True

        if self.rect.y > 600:
            self.kill()
            self.dead = True





    def event_loop(self, keys):
        for key in DIRECT_DICT:
            if keys[key]:
                self.rect.x += DIRECT_DICT[key] * self.speed

        if keys[pg.K_SPACE]:
            self.jump()

        if keys[pg.K_RIGHT]:
            self.image = self.right_image
            self.moving_right = True
        elif keys[pg.K_LEFT]:
            self.image = self.left_image
            self.moving_right = False



    def jump(self):
        if self.ok_to_jump:
            self.y_vel = self.jump_power
            self.ok_to_jump = False




    def adjust_camera(self, camera_adjust):
        self.rect.right -= camera_adjust






