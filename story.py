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
    
    # Rectangle for back to main menu button
    backToMenuButtonRect = pygame.Rect(buttonLocX, buttonLocY, buttonWithOffsetW, buttonWithOffsetH)

    # Fill STORY_WINDOW background and get mouse position
    startColor = ImageColor.getcolor(utl.COLORSCHEME[h.Scheme("BACKGROUND")], "RGB")
    endColor = ImageColor.getcolor(utl.COLORSCHEME[h.Scheme("BACKGROUND2")], "RGB")
    gradient.fillGradient(utl.STORY_WINDOW, startColor, endColor)
    h.drawBorder(utl.STORY_WINDOW)
    
    # utl.STORY_WINDOW.fill(utl.COLORSCHEME[h.Scheme("BACKGROUND")])
    mouse = pygame.mouse.get_pos()
    
    # Back to main menu button interior (hover or no hover)
    if backToMenuButtonRect.collidepoint(mouse):
        pygame.draw.rect(utl.STORY_WINDOW, button_light, backToMenuButtonRect, border_radius=3)
        utl.STORY_WINDOW.blit(text_button_light_back_main, text_button_light_back_main.get_rect(center = backToMenuButtonRect.center))
    else:
        pygame.draw.rect(utl.STORY_WINDOW, button_dark, backToMenuButtonRect, border_radius=3)
        utl.STORY_WINDOW.blit(text_button_dark_back_main, text_button_dark_back_main.get_rect(center = backToMenuButtonRect.center))
        
    # Back to main menu story button outline
    pygame.draw.rect(utl.STORY_WINDOW, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")], backToMenuButtonRect, 2, 3)
    
    return backToMenuButtonRect
