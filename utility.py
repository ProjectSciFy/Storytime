import pygame
pygame.font.init()

'''''''''''''''''
'               '
'   CONSTANTS   '
'               '
'''''''''''''''''
COLOR_SCHEME_FILE_NAME = "Colorschemes.txt"
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
RESOLUTION = (WINDOW_WIDTH, WINDOW_HEIGHT)
STORY_WINDOW = pygame.display.set_mode(RESOLUTION)
MAIN_MENU_WINDOW = pygame.display.set_mode(RESOLUTION)
in_main_window = True
Scheme = "Original"
Font = "Verdana"
Sound = "Enable"
storyLine = 0
font_size = 30
font_size_small = 22
SysFont = pygame.font.SysFont(Font,font_size)
SysSmallFont = pygame.font.SysFont(Font,font_size_small)
BUTTON_EXPAND_BUFFER = 5
MAIN_COLOR_SCHEME = 1
# COLOR SCHEME:
# Color order:
#   colorscheme[0]-Main background:                 Light
#   colorscheme[1]-Extra1
#   colorscheme[2]-Button:              Hover       Light
#   colorscheme[3]-Button:              No hover    Dark
#   colorscheme[4]-Background gradient              Dark
#   colorscheme[5]-Text/Outlines:       No hover    Dark
#   colorscheme[6]-Text/Outlines:       Hover       Light
#   colorscheme[7]-Extra2
colorscheme = []
