"""
This module initializes the display and creates dictionaries of resources.
"""

import os
import pygame as pg
from . import tools


SCREEN_SIZE = 800,600
ORIGINAL_CAPTION = "A Side-Scrolling Adventure"

#Initialization
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

#Locations of widgets during gameplay
CELL_SIZE = (72,72)
GRID_MARGIN = (75,165)
SELECTOR_MARGIN = (150,0)

#Resource loading (Fonts and music just contain path names).
FONTS = tools.load_all_fonts(os.path.join("resources","fonts"))
MUSIC = tools.load_all_music(os.path.join("resources","music"))
GFX   = tools.load_all_gfx(os.path.join("resources","graphics"))
SFX   = tools.load_all_sfx(os.path.join("resources","sound"))
