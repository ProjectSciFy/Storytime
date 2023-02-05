import pygame
from enum import Enum
pygame.init()
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
SCREEN = pygame.display.set_mode(RESOLUTION)
FONT = pygame.font.SysFont('Arial',35)
# COLOR SCHEME:
# Color order:
#   colorscheme[0]-Main background:              Light
#   colorscheme[1]-Extra1
#   colorscheme[2]-Button:           Hover       Light
#   colorscheme[3]-Button:           No hover    Dark
#   colorscheme[4]-Extra2
#   colorscheme[5]-Text/Outlines:    No hover    Dark
#   colorscheme[6]-Text/Outlines:    Hover       Light
#   colorscheme[7]-Extra3
COLORSCHEME = ['#D5ECDC', "#000000", '#CEDED5', '#B6CEC1', "#000000", '#A4A28E', '#72705B', "#000000"]
def Scheme(component: str):
    item = component.upper()
    if item == "BACKGROUND":
        return 0
    elif item == "EXTRA1":
        return 1
    elif item == "BUTTON_HOVER":
        return 2
    elif item == "BUTTON_NO_HOVER":
        return 3
    elif item == "EXTRA2":
        return 4
    elif item == "TEXT_NO_HOVER":
        return 5
    elif item == "TEXT_HOVER":
        return 6
    elif item == "EXTRA3":
        return 7
    elif item == "OUTLINE_NO_HOVER":
        return 5
    elif item == "OUTLINE_HOVER":
        return 6
    else:
        print("\nERROR: Tried to access the color scheme with the color of a nonexistant component.\n")
        return -1
    
'''''''''''''''''
'               '
' COLOR SCHEMES '
'               '
'''''''''''''''''
def loadColorSchemes() -> list:
    f = open(COLOR_SCHEME_FILE_NAME, "r")
    colorschemes = list()
    
    for scheme in f.readlines():
        colorschemes.append(scheme.replace("\",", ",").replace("\"]", "").replace("\t", "").replace("\n", "").replace(" ", "").replace("[", "").replace("\"", "#").split(","))
    return colorschemes

def displaySchemes():
    colorschemes = loadColorSchemes()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                breakpoint
        # IMPORTMANT NUMBERS:
        x_offset = 20
        y_offset = 80
        locx = 280
        locy = -60
        size = 50
        offset = 5
        schemNum = 1
        # Print squares of each color scheme
        for scheme in colorschemes:
            text_button = FONT.render(f"Color Scheme #{schemNum}:" , True, "#ffffff")
            locx = 280
            locy += y_offset
            SCREEN.blit(text_button, (x_offset + offset, locy + offset))
            for color in scheme:
                x = locx
                y = locy
                pygame.draw.rect(SCREEN, color, pygame.Rect(x, y, 60, 60), border_radius=3)
                locx += size + x_offset
            schemNum += 1
        pygame.display.update()

# Color order:
#   0-Main background:              Light
#   1-Extra1
#   2-Button:           Hover       Light
#   3-Button:           No hover    Dark
#   4-Extra2
#   5-Text/Outlines:    No hover    Dark
#   6-Text/Outlines:    Hover       Light
#   7-Extra3
#
# n: row number of color scheme in "Colorscheme.txt"
def applyColorScheme(n, order=[0,1,2,3,4,5,6,7]):
    loadScheme = loadColorSchemes()[n-1]
    background = loadScheme[order[0]]
    extra1 = loadScheme[order[1]]
    button_light = loadScheme[order[2]]
    button_dark = loadScheme[order[3]]
    extra2 = loadScheme[order[4]]
    text_light = loadScheme[order[5]]
    text_dark = loadScheme[order[6]]
    extra3 = loadScheme[order[7]]
    return [background, extra1, button_light, button_dark, extra2, text_light, text_dark, extra3]

def checkHover(pyButton: pygame.Surface, pyMouse: pygame.mouse, locx: int, locy: int, offx=0, offy=0) -> bool:
    hovering = False
    inBoundX = (locx/2-pyButton.get_width()/2) - offx/2 <= pyMouse[0] <= (locx/2+pyButton.get_width()/2) + offx/2
    inBoundY = (locy/2-pyButton.get_height()/2) - offy/2 <= pyMouse[1] <= (locy/2+pyButton.get_height()/2) + offy/2
    if inBoundX and inBoundY:
        hovering = True
    return hovering

def test():
    width = SCREEN.get_width()
    height = SCREEN.get_height()
    # Grab colors from color scheme
    button_light = COLORSCHEME[Scheme("BUTTON_HOVER")]
    button_dark = COLORSCHEME[Scheme("BUTTON_NO_HOVER")]
    # Render colors, text, and font for quit button (hover/no hover) and main menu text message
    text_button_dark = FONT.render('Quit' , True , COLORSCHEME[Scheme("TEXT_NO_HOVER")])
    text_button_light = FONT.render('Quit' , True , COLORSCHEME[Scheme("TEXT_HOVER")])
    text_main_menu = FONT.render('Welcome to Storytime!' , True , COLORSCHEME[Scheme("TEXT_NO_HOVER")])

    while True:
        # Create quit button text, outline, filling, and hovering variables
        button_h = text_button_dark.get_height()
        button_w = text_button_dark.get_width()
        offset_h = text_button_dark.get_height()//5
        offset_w = text_button_dark.get_width()//2
        midButtonW = width/2 - button_w/2
        midButtonH = height/2 - button_h/2
        buttonLocX = midButtonW - offset_w/2
        buttonLocY = midButtonH - offset_h/2
        buttonWithOffsetW = button_w + offset_w
        buttonWithOffsetH = button_h + offset_h
        # Rectangle for quit button
        quitButtonRect = [buttonLocX, buttonLocY, buttonWithOffsetW, buttonWithOffsetH]
        
        # Fill screen background and get mouse position
        SCREEN.fill(COLORSCHEME[Scheme("BACKGROUND")])
        mouse = pygame.mouse.get_pos()
        
        # Quit button interior (hover or no hover)
        if checkHover(text_button_dark, mouse, width, height, offset_w, offset_h):
            pygame.draw.rect(SCREEN, button_light, quitButtonRect, border_radius=3)
            SCREEN.blit(text_button_light, (midButtonW, midButtonH))
        else:
            pygame.draw.rect(SCREEN, button_dark, quitButtonRect, border_radius=3)
            SCREEN.blit(text_button_dark, (midButtonW, midButtonH))
            
        # Quit button outline
        pygame.draw.rect(SCREEN, COLORSCHEME[6], quitButtonRect, 2, 3)
        
        
        # Main menu text message
        mainMenuTextLocX = width/2 - text_main_menu.get_width()/2
        mainMenuTextLocY = height/2 - text_main_menu.get_height()/2-100
        SCREEN.blit(text_main_menu, (mainMenuTextLocX, mainMenuTextLocY))
        
        # Check for any button pushes or program closure
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if checkHover(text_button_dark, mouse, SCREEN.get_width(), SCREEN.get_height()):
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()
        
''''''''''''''''''''''''''''''''''''
        
#If you uncomment this line, you must comment out all lines below this function (they will be unreachable.)

#Un-comment the line below to see all color schemes in "Colorschemes.txt".
displaySchemes()

''''''''''''''''''''''''''''''''''''

#Change the "1" argument in the line below to "2" to try the second color scheme from "Colorschemes.txt".
#You will need both line 152 and 153 un-commented in order to test the color schemes in "Colorschemes.txt".

#Un-comment the line below to change color schemes
# COLORSCHEME = applyColorScheme(1)
# test()
