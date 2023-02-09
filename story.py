import pygame
import utility as utl
import helpers as h
pygame.init()
pygame.font.init()

# Grab colors from color scheme
button_light = utl.COLORSCHEME[h.Scheme("BUTTON_HOVER")]
button_dark = utl.COLORSCHEME[h.Scheme("BUTTON_NO_HOVER")]
# Render colors, text, and font for screen swap button (hover/no hover) and main menu text message
text_button_dark = utl.FONT.render('View Story' , True , utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
text_button_light = utl.FONT.render('View Story' , True , utl.COLORSCHEME[h.Scheme("TEXT_HOVER")])
text_button_dark_back_main = utl.FONT.render('Go to Main Menu' , True , utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
text_button_light_back_main = utl.FONT.render('Go to Main Menu' , True , utl.COLORSCHEME[h.Scheme("TEXT_HOVER")])
utl.FONT.set_bold(True)
utl.FONT.set_underline(True)
text_main_menu = utl.FONT.render('Welcome to Storytime!' , True , utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
text_select_menu = utl.FONT.render('Customize Story:' , True , utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
text_story = utl.FONT.render('Story Time!' , True , utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")])
utl.FONT.set_bold(False)
utl.FONT.set_underline(False)
# Dropdowns setup
numDropdowns = 2
dropdownX = 30
dropdownWidth = 300
dropdownHeight = 50
dropdownY = list()
dropdownBuffer = 30

def updateStory(event_list: list):
    # Create screen swap button text, outline, filling, and hovering variables
    sideBarLWidth = 0
    button_h = text_button_dark_back_main.get_height()
    button_w = text_button_dark_back_main.get_width()
    offset_h = text_button_dark_back_main.get_height()//5
    offset_w = text_button_dark_back_main.get_width()//2
    midButtonW = utl.WINDOW_WIDTH/2 - button_w/2 + sideBarLWidth/2
    midButtonH = utl.WINDOW_HEIGHT/2 - button_h/2
    buttonLocX = midButtonW - offset_w/2
    buttonLocY = midButtonH - offset_h/2
    buttonWithOffsetW = button_w + offset_w
    buttonWithOffsetH = button_h + offset_h
    
    # Rectangle for back to main menu button
    backToMenuButtonRect = pygame.Rect(buttonLocX, buttonLocY, buttonWithOffsetW, buttonWithOffsetH)

    # Fill STORY_WINDOW background and get mouse position
    utl.STORY_WINDOW.fill(utl.COLORSCHEME[h.Scheme("BACKGROUND")])
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
    
    # Story time text message
    storyTextLocX = utl.WINDOW_WIDTH/2 - text_story.get_width()/2 + sideBarLWidth/2
    storyTextLocY = utl.WINDOW_HEIGHT/2 - text_story.get_height()/2-100
    utl.STORY_WINDOW.blit(text_story, (storyTextLocX, storyTextLocY))
    
    return backToMenuButtonRect