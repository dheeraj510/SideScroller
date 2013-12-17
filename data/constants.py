__author__ = 'justinarmstrong'

## COLORS ##

#            R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)

BGCOLOR = NEAR_BLACK


##Runner Constants##

RUNNER_WIDTH = 20
RUNNER_HEIGHT = 40
RUNNER_NAME = 'runner'
RUNNER_SPEED = 5
JUMP_SPEED = 10
FALL_SPEED = 10
MAX_HEIGHT = 175
JUMP_POWER = -9

STARTY = 500
STARTX = 100
CAMERA_XPOINT = 400


##Ground Constants##

GROUND_WIDTH = 80
GROUND_HEIGHT = 100


##Platform Constants##

PLAT_WIDTH = 80
PLAT_HEIGHT = 20
PLAT1_STARTX = 600
PLAT1_STARTY = STARTY - 100

PLAT2_STARTX = PLAT1_STARTX + 100
PLAT2_STARTY = PLAT1_STARTY - 100

PLAT3_STARTX = PLAT2_STARTX + 100
PLAT3_STARTY = PLAT2_STARTY - 100
