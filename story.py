import pygame
from PIL import ImageColor
import utility as utl
import helpers as h
import gradient
pygame.init()
pygame.font.init()

def updateStory(event_list: list):
    # Grab colors from color scheme
    button_light = utl.colorscheme[h.Scheme("BUTTON_HOVER")]
    button_dark = utl.colorscheme[h.Scheme("BUTTON_NO_HOVER")]
    # Render colors, text, and font for screen swap button (hover/no hover) and main menu text message
    text_button_dark_back_main = utl.SysFont.render('Back to Main Menu' , True , utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
    text_button_light_back_main = utl.SysFont.render('Back to Main Menu' , True , utl.colorscheme[h.Scheme("TEXT_HOVER")])

    # button surfaces for back and forward arrows 
    back_arrow_button_dark = utl.SysSmallFont.render('<', True, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
    back_arrow_button_light = utl.SysSmallFont.render("<", True, utl.colorscheme[h.Scheme("TEXT_HOVER")])
    forward_arrow_button_dark = utl.SysSmallFont.render('>', True, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
    forward_arrow_button_light = utl.SysSmallFont.render(">", True, utl.colorscheme[h.Scheme("TEXT_HOVER")])
    
    # Create screen swap button text, outline, filling, and hovering variables
    button_h = text_button_dark_back_main.get_height()
    button_w = text_button_dark_back_main.get_width()
    offset_h = text_button_dark_back_main.get_height()//5
    offset_w = text_button_dark_back_main.get_width()//2
    buttonLocX = utl.WINDOW_WIDTH/2 - button_w/2 - offset_w/2
    buttonLocY = 0
    buttonWithOffsetW = button_w + offset_w
    buttonWithOffsetH = button_h + offset_h

    # creating rectangle for photos 
    # x, y
    # random numbers right now
    storyRect = pygame.Rect(300, 150, 500, 300)
    forwardArrowRect = pygame.Rect(850, 250, 50, 80)
    backArrowRect = pygame.Rect(200, 250, 50, 80)
    textStoryRect = pygame.Rect(100, 500, 900, 100)
    # load in image 
    #   need to determine size of image, and placement in rectangle 
    image = pygame.image.load("skate_cat.jpg")
    image2 = pygame.image.load("brutus_buckeye.jpeg")
    # need to do math to figure out proper dimensions of an image... centering it in story rect. 
    image = pygame.transform.scale(image, (300, 250))
    image2 = pygame.transform.scale(image2, (300, 250))
    # load in a text file. Right now 1 sentence per line. 
    images = [image, image2]
    inputFile = open('story_text.txt', 'r')
    storyText = []
    for line in inputFile: 
        storyText.append(line.replace('\n', " "))
    
    numOfEntries = len(storyText)

    
    
    # Rectangle for back to main menu button
    backToMenuButtonRect = pygame.Rect(buttonLocX, buttonLocY, buttonWithOffsetW, buttonWithOffsetH)

    # Fill STORY_WINDOW background and get mouse position
    startColor = ImageColor.getcolor(utl.colorscheme[h.Scheme("BACKGROUND")], "RGB")
    endColor = ImageColor.getcolor(utl.colorscheme[h.Scheme("BACKGROUND2")], "RGB")
    gradient.fillGradient(utl.STORY_WINDOW, startColor, endColor)
    h.drawBorder(utl.STORY_WINDOW)
    
    # utl.STORY_WINDOW.fill(utl.COLORSCHEME[h.Scheme("BACKGROUND")])
    mouse = pygame.mouse.get_pos()
    
    # Back to main menu button interior (hover or no hover)
    if backToMenuButtonRect.collidepoint(mouse):
        pygame.draw.rect(utl.STORY_WINDOW, button_light, backToMenuButtonRect, border_radius=3)
        utl.STORY_WINDOW.blit(text_button_light_back_main, text_button_light_back_main.get_rect(center = backToMenuButtonRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_HOVER")], backToMenuButtonRect, 2, 3)
    else:
        pygame.draw.rect(utl.STORY_WINDOW, button_dark, backToMenuButtonRect, border_radius=3)
        utl.STORY_WINDOW.blit(text_button_dark_back_main, text_button_dark_back_main.get_rect(center = backToMenuButtonRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")], backToMenuButtonRect, 2, 3)
    
    # hover or no hover for back arrow 
    if backArrowRect.collidepoint(mouse) and utl.storyLine != 0: 
        pygame.draw.rect(utl.STORY_WINDOW, button_light, backArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(back_arrow_button_light, back_arrow_button_light.get_rect(center = backArrowRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_HOVER")], backArrowRect, 2, 3)
    else: 
        pygame.draw.rect(utl.STORY_WINDOW, button_dark, backArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(back_arrow_button_dark, back_arrow_button_dark.get_rect(center = backArrowRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")], backArrowRect, 2, 3)

    # hover or no over for forward arrow 
    if forwardArrowRect.collidepoint(mouse) and utl.storyLine != numOfEntries-1: 
        pygame.draw.rect(utl.STORY_WINDOW, button_light, forwardArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(forward_arrow_button_light, forward_arrow_button_light.get_rect(center = forwardArrowRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_HOVER")], forwardArrowRect, 2, 3)
    else: 
        pygame.draw.rect(utl.STORY_WINDOW, button_dark, forwardArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(forward_arrow_button_dark, forward_arrow_button_dark.get_rect(center = forwardArrowRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")], forwardArrowRect, 2, 3)
 

    pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], textStoryRect, 2, 3)
    pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], storyRect, 2, 3 )


    utl.STORY_WINDOW.blit(image, (400, 175))
    text = utl.SysFont.render(storyText[utl.storyLine], True, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
    utl.STORY_WINDOW.blit(text, (105, 500))
    textUpdate = False
    for event in event_list: 
        if event.type == pygame.MOUSEBUTTONDOWN and backArrowRect.collidepoint(mouse) and utl.storyLine != 0: 
            utl.storyLine = utl.storyLine -1

        elif event.type == pygame.MOUSEBUTTONDOWN and forwardArrowRect.collidepoint(mouse) and utl.storyLine != numOfEntries-1: 
            utl.storyLine = utl.storyLine +1 

    text = utl.SysFont.render(storyText[utl.storyLine], True, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
    utl.STORY_WINDOW.blit(text, (105, 500))
    utl.STORY_WINDOW.blit(images[utl.storyLine], (400, 175))
    
    return backToMenuButtonRect
