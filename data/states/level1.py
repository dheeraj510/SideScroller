__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import tools
from .. import constants
from .. components import runner,ground,platform


class Level_1(tools._State):
    """This state is updated when the game is on Level 1"""
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persistant):
        self.setup_runner()
        self.setup_ground()
        self.setup_platforms()
        self.jump_on_sprites = pg.sprite.Group(self.ground,
                                               self.platforms)
        self.allSprites = pg.sprite.Group(self.runner,
                                          self.ground,
                                          self.platforms)
        self.camera_adjust_x = 0

    def setup_runner(self):
        self.runner = runner.Runner()
        self.runner.rect.x = constants.STARTX
        self.runner.rect.bottom = constants.STARTY

    def setup_ground(self):
        ground_list = []
        for i in range(20):
            ground_list.append(ground.Ground())

        for i in range(len(ground_list)):
            ground_list[i].rect.x += i * constants.GROUND_WIDTH
            ground_list[i].rect.y = constants.STARTY

        self.ground = pg.sprite.Group(ground_list)


    def setup_platforms(self):
        platform1 = platform.Platform()
        platform1.rect.x = constants.PLAT1_STARTX
        platform1.rect.y = constants.PLAT1_STARTY
        self.platforms = pg.sprite.Group(platform1)


    def camera(self):
        if self.runner.rect.right > constants.CAMERA_XPOINT:
            self.camera_adjust_x = (self.runner.rect.right -
                                    constants.CAMERA_XPOINT)
        elif self.runner.rect.left < constants.STARTX:
            self.camera_adjust_x = (self.runner.rect.left - constants.STARTX)

        else:
            self.camera_adjust_x = 0


    def update(self, surface, keys, current_time):
        """Updates level"""
        self.current_time = current_time
        setup.SCREEN.fill(constants.BGCOLOR)
        self.camera()
        self.allSprites.update(keys, self.camera_adjust_x)
        self.runner.collision(self.jump_on_sprites)
        self.allSprites.draw(surface)




