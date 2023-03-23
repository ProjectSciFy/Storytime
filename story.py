import pygame
import sounds
from PIL import ImageColor
import utility as utl
import helpers as h
import gradient
pygame.init()
pygame.font.init()

# Grab colors from color scheme
button_light = utl.COLORSCHEME[h.Scheme("BUTTON_HOVER")]
button_dark = utl.COLORSCHEME[h.Scheme("BUTTON_NO_HOVER")]
# Render colors, text, and font for screen swap button (hover/no hover) and main menu text message
text_button_dark_back_main = utl.FONT.render('Back to Main Menu' , True , utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
text_button_light_back_main = utl.FONT.render('Back to Main Menu' , True , utl.COLORSCHEME[h.Scheme("TEXT_HOVER")])

# button surfaces for back and forward arrows 
back_arrow_button_dark = utl.FONT.render('<', True, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
back_arrow_button_light = utl.FONT.render("<", True, utl.COLORSCHEME[h.Scheme("TEXT_HOVER")])
forward_arrow_button_dark = utl.FONT.render('>', True, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
forward_arrow_button_light = utl.FONT.render(">", True, utl.COLORSCHEME[h.Scheme("TEXT_HOVER")])


def updateStory(event_list: list):
    # Create screen swap button text, outline, filling, and hovering variables
    button_h = text_button_dark_back_main.get_height()
    button_w = text_button_dark_back_main.get_width()
    offset_h = text_button_dark_back_main.get_height()//5
    offset_w = text_button_dark_back_main.get_width()//2
    buttonLocX = utl.WINDOW_WIDTH/2 - button_w/2 - offset_w/2
    buttonLocY = 0
    buttonWithOffsetW = button_w + offset_w
    buttonWithOffsetH = button_h + offset_h

    # for y positions, divide screen into fifths 
    story_rect_xpos = utl.WINDOW_WIDTH/2 
    story_rect_ypos = 2 * utl.WINDOW_HEIGHT/5
    story_text_ypos = 4 * utl.WINDOW_HEIGHT/5

    # creating rectangle for photos 
    # storyRect = pygame.Rect(300, 150, 500, 300)
    storyRect = pygame.Rect(0, 0, 600, 350)
    storyRect.center = (story_rect_xpos, story_rect_ypos)
    # forwardArrowRect = pygame.Rect(850, 250, 50, 80)
    forwardArrowRect = pygame.Rect(0, 0, 50, 80)
    forwardArrowRect.center = (900, story_rect_ypos)
    # backArrowRect = pygame.Rect(200, 250, 50, 80)
    backArrowRect = pygame.Rect(0, 0, 50, 80)
    backArrowRect.center = (200, story_rect_ypos)
    # textStoryRect = pygame.Rect(100, 500, 900, 100)
    textStoryRect = pygame.Rect(0, 0, 900, 100)
    textStoryRect.center = (story_rect_xpos, story_text_ypos)

    # load in image 
    #   need to determine size of image, and placement in rectangle 
    image = pygame.image.load("skate_cat.jpg")
    image2 = pygame.image.load("brutus_buckeye.jpeg")
 
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
    startColor = ImageColor.getcolor(utl.COLORSCHEME[h.Scheme("BACKGROUND")], "RGB")
    endColor = ImageColor.getcolor(utl.COLORSCHEME[h.Scheme("BACKGROUND2")], "RGB")
    gradient.fillGradient(utl.STORY_WINDOW, startColor, endColor)
    h.drawBorder(utl.STORY_WINDOW)

    mouse = pygame.mouse.get_pos()
    
    # Back to main menu button interior (hover or no hover)
    if backToMenuButtonRect.collidepoint(mouse):
        pygame.draw.rect(utl.STORY_WINDOW, button_light, backToMenuButtonRect, border_radius=3)
        utl.STORY_WINDOW.blit(text_button_light_back_main, text_button_light_back_main.get_rect(center = backToMenuButtonRect.center))
    else:
        pygame.draw.rect(utl.STORY_WINDOW, button_dark, backToMenuButtonRect, border_radius=3)
        utl.STORY_WINDOW.blit(text_button_dark_back_main, text_button_dark_back_main.get_rect(center = backToMenuButtonRect.center))
    
    # hover or no hover for back arrow, only allow hover if its possible to go back
    if backArrowRect.collidepoint(mouse) and utl.storyLine != 0: 
        pygame.draw.rect(utl.STORY_WINDOW, button_light, backArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(back_arrow_button_light, back_arrow_button_light.get_rect(center = backArrowRect.center))
    else: 
        pygame.draw.rect(utl.STORY_WINDOW, button_dark, backArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(back_arrow_button_dark, back_arrow_button_dark.get_rect(center = backArrowRect.center))

    # hover or no over for forward arrow, only allow hover if its possible to go forward
    if forwardArrowRect.collidepoint(mouse) and utl.storyLine != numOfEntries-1: 
        pygame.draw.rect(utl.STORY_WINDOW, button_light, forwardArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(forward_arrow_button_light, forward_arrow_button_light.get_rect(center = forwardArrowRect.center))
    else: 
        pygame.draw.rect(utl.STORY_WINDOW, button_dark, forwardArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(forward_arrow_button_dark, forward_arrow_button_dark.get_rect(center = forwardArrowRect.center))
 


    pygame.draw.rect(utl.STORY_WINDOW, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")], textStoryRect, 2, 3)
    pygame.draw.rect(utl.STORY_WINDOW, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")], forwardArrowRect, 2, 3)
    pygame.draw.rect(utl.STORY_WINDOW, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")], backArrowRect, 2, 3)
    pygame.draw.rect(utl.STORY_WINDOW, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")], storyRect, 2, 3 )

    # Back to main menu story button outline
    pygame.draw.rect(utl.STORY_WINDOW, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")], backToMenuButtonRect, 2, 3)
    
    # need to determine exact positioning of images and text, will figure out after we see what comes in from api
    utl.STORY_WINDOW.blit(image, (400, 165))
    text = utl.FONT.render(storyText[utl.storyLine], True, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
    utl.STORY_WINDOW.blit(text, (100, 515))

    for event in event_list: 
        if event.type == pygame.MOUSEBUTTONDOWN and backArrowRect.collidepoint(mouse) and utl.storyLine != 0: 
            utl.storyLine = utl.storyLine -1
 
        elif event.type == pygame.MOUSEBUTTONDOWN and forwardArrowRect.collidepoint(mouse) and utl.storyLine != numOfEntries-1: 
            utl.storyLine = utl.storyLine +1 

    # need to determine exact positioning of images and text, will figure out after we see what comes in from api
    text = utl.FONT.render(storyText[utl.storyLine], True, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
    utl.STORY_WINDOW.blit(text, (100, 515))
    utl.STORY_WINDOW.blit(images[utl.storyLine], (400, 165))
    
    return backToMenuButtonRect
