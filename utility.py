import pygame
import sounds as s
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
FONT_SIZE = 30
FONT_SIZE_SMALL = 24
FONT = pygame.font.SysFont('Verdana',FONT_SIZE)
SMALL_FONT = pygame.font.SysFont('Verdana',FONT_SIZE_SMALL)
BUTTON_EXPAND_BUFFER = 5
MAIN_COLOR_SCHEME = 5
Genre = ""
Length = ""
Language = ""
storyLine = 0
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
COLORSCHEME = ["#dfd1d3", "#f5e6e8", "#d5c6e0", "#aaa1c8", "#967aa1", "#192a51", "#2e3d61", "#414f6f"]
