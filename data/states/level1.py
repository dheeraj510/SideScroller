__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import tools
from .. import constants as con
from .. components import runner,ground,platform,coin


class Level_1(tools._State):
    """This state is updated when the game is on Level 1"""
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persistant, coin_count=0):
        self.setup_runner()
        self.setup_ground()
        self.setup_platforms()
        self.setup_coins()
        self.ground_and_platforms = pg.sprite.Group(self.ground,
                                               self.platforms)
        self.allSprites = pg.sprite.Group(self.runner,
                                          self.ground,
                                          self.platforms,
                                          self.coins)
        self.camera_adjust_x = 0
        self.coin_count = coin_count

    def setup_runner(self):
        self.runner = runner.Runner()
        self.runner.rect.x = con.STARTX
        self.runner.rect.bottom = con.STARTY

    def setup_ground(self):
        ground_list = []
        for i in range(20):
            ground_list.append(ground.Ground())
            ground_list[i].rect.x += i * con.GROUND_WIDTH
            ground_list[i].rect.y = con.STARTY

        self.ground = pg.sprite.Group(ground_list)

        for block in self.ground:
            if block.rect.x > 480 and block.rect.x < 1000:
                block.kill()


    def setup_platforms(self):
        platform1 = platform.Platform(con.PLAT1_STARTX, con.PLAT1_STARTY, True)
        platform2 = platform.Platform(con.PLAT2_STARTX, con.PLAT2_STARTY)
        platform3 = platform.Platform(con.PLAT3_STARTX, con.PLAT3_STARTY)
        platform4 = platform.Platform(1000, con.PLAT3_STARTY)
        platform5 = platform.Platform(1175, con.PLAT3_STARTY, True)


        self.platforms = pg.sprite.Group(platform1, platform2, platform3,
                                         platform4, platform5)


    def setup_coins(self):
        coin1 = coin.Coin(1025, 100)
        coin2 = coin.Coin(1200, 100)

        self.coins = pg.sprite.Group(coin1, coin2)


    def camera(self):
        if self.runner.rect.right > con.CAMERA_XPOINT:
            self.camera_adjust_x = (self.runner.rect.right -
                                    con.CAMERA_XPOINT)
        elif self.runner.rect.left < con.STARTX:
            self.camera_adjust_x = (self.runner.rect.left - con.STARTX)

        else:
            self.camera_adjust_x = 0


    def check_for_reset(self):
        current_time = None
        persistant = None

        if self.runner.dead == True:
            self.runner.dead = False
            self.startup(current_time, persistant, self.coin_count)


    def check_for_coins(self):
        runner = pg.sprite.Group(self.runner)
        pg.sprite.groupcollide(runner, self.coins, False, True)
        self.coin_count += 1



    def update(self, surface, keys, current_time):
        """Updates level"""
        self.current_time = current_time
        setup.SCREEN.fill(con.BGCOLOR)
        self.camera()
        self.allSprites.update(keys, self.camera_adjust_x, self.ground_and_platforms)
        self.allSprites.draw(surface)
        self.check_for_coins()
        self.check_for_reset()




