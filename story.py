import pygame
from PIL import ImageColor
import generate as gen
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

    # Create story and scrolling buttons rectangles
    storyRect = pygame.Rect(300, 59, 512, 512)
    forwardArrowRect = pygame.Rect(837, 285, 50, 80)
    backArrowRect = pygame.Rect(225, 285, 50, 80)
    textStoryRect = pygame.Rect(50, 588, 970, 100)
    
    
    '''BUILD STORY:'''
    ### UNCOMMENT THIS TO GENERATE NEW STORY IMAGES FROM TEXT IN 'tempt.txt'. ###
    ### CHANGE '2' PARAMETER ON LINE 43 TO CONTROL STORY NUMBER. ###
    # story = gen.generateSampleStory(2)
    # h.updateStoryText(story[0])
    # h.updateStoryImages(story[1])
    
    ### CREATE LIST OF STORY TEXT SENTENCES AND STORY IMAGES. ###
    # storyIndex = 0
    # s = h.readTestStories("temp.txt")[0].split(".")
    # storyText = list()
    # numOfEntries = len(s)
    # for sentence in s:
    #     if len(sentence) > 1:
    #         storyText.append(sentence.strip() + ".")
    #     else:
    #         numOfEntries -= 1
    # images = [pygame.transform.scale(pygame.image.load(f"./images/story_{storyIndex}/sentence_{i}.png"), (508, 508)) for i in range(numOfEntries)]
    ''''''''''''''''''
    
    '''BACKGROUND: '''
    # Fill STORY_WINDOW background and get mouse position
    startColor = ImageColor.getcolor(utl.colorscheme[h.Scheme("BACKGROUND")], "RGB")
    endColor = ImageColor.getcolor(utl.colorscheme[h.Scheme("BACKGROUND2")], "RGB")
    gradient.fillGradient(utl.STORY_WINDOW, startColor, endColor)
    h.drawBorder(utl.STORY_WINDOW)
    ''''''''''''''''''
    
    '''MOUSE STUFF:'''
    # utl.STORY_WINDOW.fill(utl.COLORSCHEME[h.Scheme("BACKGROUND")])
    mouse = pygame.mouse.get_pos()
    ''''''''''''''''''
    
    '''''BUTTONS:'''''
    # Rectangle for back to main menu button
    backToMenuButtonRect = pygame.Rect(buttonLocX, buttonLocY, buttonWithOffsetW, buttonWithOffsetH)
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
    if backArrowRect.collidepoint(mouse) and utl.storyLine > 0: 
        pygame.draw.rect(utl.STORY_WINDOW, button_light, backArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(back_arrow_button_light, back_arrow_button_light.get_rect(center = backArrowRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_HOVER")], backArrowRect, 2, 3)
    else: 
        pygame.draw.rect(utl.STORY_WINDOW, button_dark, backArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(back_arrow_button_dark, back_arrow_button_dark.get_rect(center = backArrowRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")], backArrowRect, 2, 3)
    # hover or no over for forward arrow 
    if forwardArrowRect.collidepoint(mouse) and utl.storyLine <= len(utl.storyText)-1: 
        pygame.draw.rect(utl.STORY_WINDOW, button_light, forwardArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(forward_arrow_button_light, forward_arrow_button_light.get_rect(center = forwardArrowRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_HOVER")], forwardArrowRect, 2, 3)
    else: 
        pygame.draw.rect(utl.STORY_WINDOW, button_dark, forwardArrowRect, border_radius=3)
        utl.STORY_WINDOW.blit(forward_arrow_button_dark, forward_arrow_button_dark.get_rect(center = forwardArrowRect.center))
        pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")], forwardArrowRect, 2, 3)
    ''''''''''''''''''
    
    '''''OUTLINES'''''
    pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], textStoryRect, border_radius = 3, width = 2)
    pygame.draw.rect(utl.STORY_WINDOW, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], storyRect, border_radius = 3, width = 0)
    ''''''''''''''''''
    
    '''STORY STUFF:'''
    text = ""
    if len(utl.storyText) > 0:
        text = utl.SysFont.render(utl.storyText[utl.storyLine], True, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
    # textUpdate = False
    for event in event_list: 
        if event.type == pygame.MOUSEBUTTONDOWN and backArrowRect.collidepoint(mouse) and utl.storyLine > 0: 
            utl.storyLine -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN and forwardArrowRect.collidepoint(mouse) and utl.storyLine <= len(utl.storyText)-1: 
            utl.storyLine += 1 
            
    rect = textStoryRect
    y = rect.top
    lineSpacing = -2
    fontHeight = utl.SysSmallFont.size("Tg")[1]
    if len(utl.storyText) > 0:
        text_to_render = utl.storyText[utl.storyLine]
        while text_to_render:
            i = 1
            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break
            # determine maximum width of line
            while utl.SysSmallFont.size(text_to_render[:i])[0] < rect.width - 6 and i < len(text_to_render):
                i += 1
            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text_to_render): 
                i = text_to_render.rfind(" ", 0, i) + 1
            rendered_text = utl.SysSmallFont.render(text_to_render[:i], True, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
            utl.STORY_WINDOW.blit(rendered_text, (rect.left + 5, y + 5))
            y += fontHeight + lineSpacing
            # remove the text we just blitted
            text_to_render = text_to_render[i:]
    if len(utl.storyImages) > 0:
        utl.STORY_WINDOW.blit(utl.storyImages[utl.storyLine], (302, 61))
    return backToMenuButtonRect
