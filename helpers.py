import pygame
import utility as utl
pygame.font.init()


'''''''''''''''''
'               '
' COLOR SCHEMES '
'               '
'''''''''''''''''
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
    elif item == "BACKGROUND2":
        return 4
    elif item == "TEXT_NO_HOVER":
        return 5
    elif item == "TEXT_HOVER":
        return 6
    elif item == "EXTRA2":
        return 7
    elif item == "OUTLINE_NO_HOVER":
        return 5
    elif item == "OUTLINE_HOVER":
        return 6
    else:
        print("\nERROR: Tried to access the color scheme with the color of a nonexistant component.\n")
        return -1
    
def loadColorSchemes() -> list:
    f = open(utl.COLOR_SCHEME_FILE_NAME, "r")
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
        locx = 320
        locy = -60
        size = 50
        offset = 5
        schemNum = 1
        # Print squares of each color scheme
        for scheme in colorschemes:
            text_button = utl.FONT.render(f"Color Scheme #{schemNum}:" , True, "#ffffff")
            locx = 320
            locy += y_offset
            utl.MAIN_MENU_WINDOW.blit(text_button, (x_offset + offset, locy + offset))
            for color in scheme:
                x = locx
                y = locy
                pygame.draw.rect(utl.MAIN_MENU_WINDOW, color, pygame.Rect(x, y, 60, 60), border_radius=3)
                locx += size + x_offset
            schemNum += 1
        pygame.display.update()


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
#
# n: row number of color scheme in "Colorscheme.txt"
def applyColorScheme(n, order=[0,1,2,3,4,5,6,7]):
    loadScheme = loadColorSchemes()[n-1]
    background = loadScheme[order[0]]
    extra1 = loadScheme[order[1]]
    button_light = loadScheme[order[2]]
    button_dark = loadScheme[order[3]]
    background2 = loadScheme[order[4]]
    text_light = loadScheme[order[5]]
    text_dark = loadScheme[order[6]]
    extra2 = loadScheme[order[7]]
    return [background, extra1, button_light, button_dark, background2, text_light, text_dark, extra2]

def drawBorder(surf: pygame.Surface):
    rect = pygame.Rect(0, 0, surf.get_width(), surf.get_height())
    pygame.draw.rect(surf, utl.COLORSCHEME[Scheme("TEXT_NO_HOVER")], rect, 2)
