__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import tools
from .. import constants
from .. components import runner,ground


class Level_1(tools._State):
    """This state is updated when the game is on Level 1"""
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persistant):
        self.setup_runner()
        self.setup_ground()
        self.allSprites = pg.sprite.Group(self.runner, self.ground)
        self.camera_adjust_x = 0

    def setup_runner(self):
        self.runner = runner.Runner()
        self.runner.rect.x = constants.STARTX
        self.runner.rect.bottom = constants.STARTY

    def setup_ground(self):
        ground_list = []
        for i in range(11):
            ground_list.append(ground.Ground())

        for i in range(len(ground_list)):
            ground_list[i].rect.x += i * constants.GROUND_WIDTH
            ground_list[i].rect.y = constants.STARTY

        self.ground = pg.sprite.Group(ground_list)
        self.allSprites.add(self.ground)

    def update_runner(self, keys):
        self.runner.update(keys, self.camera_adjust_x)

    def update_ground(self, keys):
        for tile in self.ground:
            tile.update(keys, self.camera_adjust_x)

            if tile.rect.left > 800 and tile.rect.right > 800:
                right_edge = tile.rect.right
                self.ground.add(ground.Ground(right_edge,
                                             constants.STARTY))
            elif tile.rect.
                del self.ground[0]
                print len(self.ground)

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
        self.update_runner(keys)
        self.update_ground(keys)
        self.camera()

        self.allSprites.draw(surface)




