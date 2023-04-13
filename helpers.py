import pygame
import utility as utl
from PIL import Image
import json

'''''''''''''''''
'               '
' COLOR SCHEMES '
'               '
'''''''''''''''''
def Scheme(component: str):
    item = component.upper()
    if item == "BACKGROUND":
        return 0
    elif item == "TEXT_RASA":
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
    elif item == "TEXT_USER":
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
            text_button = utl.SysFont.render(f"Color Scheme #{schemNum}:" , True, "#ffffff")
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
#   colorscheme[1]-Text
#   colorscheme[2]-Button:              Hover       Light
#   colorscheme[3]-Button:              No hover    Dark
#   colorscheme[4]-Background gradient              Dark
#   colorscheme[5]-Text/Outlines:       No hover    Dark
#   colorscheme[6]-Text/Outlines:       Hover       Light
#   colorscheme[7]-Text                             
#
# n: row number of color scheme in "Colorscheme.txt"
def applyColorScheme(n, order=[0,1,2,3,4,5,6,7]):
    loadScheme = loadColorSchemes()[n-1]
    background = loadScheme[order[0]]
    text_rasa = loadScheme[order[1]]
    button_light = loadScheme[order[2]]
    button_dark = loadScheme[order[3]]
    background2 = loadScheme[order[4]]
    text_light = loadScheme[order[5]]
    text_dark = loadScheme[order[6]]
    text_user = loadScheme[order[7]]
    return [background, text_rasa, button_light, button_dark, background2, text_light, text_dark, text_user]

def drawBorder(surf: pygame.Surface):
    rect = pygame.Rect(0, 0, surf.get_width(), surf.get_height())
    pygame.draw.rect(surf, utl.colorscheme[Scheme("TEXT_NO_HOVER")], rect, 2)
     
def updateScheme(Scheme: str) -> list:
    utl.scheme = Scheme
    # COLOR SCHEME UPDATE
    if Scheme.upper() == "ORIGINAL":
        utl.MAIN_COLOR_SCHEME = 1
    elif Scheme.upper() == "FOREST":
        utl.MAIN_COLOR_SCHEME = 2
    elif Scheme.upper() == "MOUNTAIN":
        utl.MAIN_COLOR_SCHEME = 3
    elif Scheme.upper() == "FIRE":
        utl.MAIN_COLOR_SCHEME = 4
    utl.colorscheme = applyColorScheme(utl.MAIN_COLOR_SCHEME) 

    with open('rasa/rasa_pass.json','r+') as f:
            data = json.load(f)
            data['scheme'] = utl.scheme
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 

    return utl.colorscheme
    
def updateFont(Font: str) -> tuple:
    #FONT UPDATE
    utl.SysFont = pygame.font.SysFont(Font, utl.font_size)
    utl.SysSmallFont = pygame.font.SysFont(Font, utl.font_size_small)

    with open('rasa/rasa_pass.json','r+') as f:
        data = json.load(f)
        data['font'] = Font
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate() 

    return (utl.SysFont, utl.SysSmallFont)
 
def updateSound(Sound: str) -> str:
    utl.Sound = Sound.upper()

    with open('rasa/rasa_pass.json','r+') as f:
        data = json.load(f)
        data['sound'] = utl.Sound
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate() 

    return utl.Sound

def updateStoryText(sentences: list) -> list:
    utl.storyText = sentences
    return utl.storyText

def updateStoryImages(images: list) -> list:
    utl.storyImages = images
    return utl.storyImages

def assertValidStory() -> bool:
    return len(utl.storyText) == len(utl.storyImages)

def readTestStories(filePath: str) -> list:
    '''
    filePath can be just "fileName" or "/path/to/fileName"
    '''
    stories = list()
    with open(filePath, 'r') as file:
        text = file.read()
        stories = text.split('---\n')
        stories = [story.strip() for story in stories]
        
    return stories

def getImage(storyIndex: int, imageIndex: int) -> list:
    return Image.open(f"./images/story_{storyIndex}/sentence_{imageIndex}.png")
    
    # image = pygame.transform.scale(pygame.image.load("skate_cat.jpg"), (508, 508))
    # return image
