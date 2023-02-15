import pygame
import sounds
from PIL import ImageColor
import utility as utl
import helpers as h
import dropdown
import gradient
import inputbox
pygame.init()
pygame.font.init()

''''''''''''''''''
'                '
' CREATE OBJECTS '
'                '
''''''''''''''''''
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
''''''''''''''''''
'                '
' DROPDOWN STUFF '
'                '
''''''''''''''''''
numDropdowns = 2
dropdownX = 30
dropdownWidth = 300
dropdownHeight = 50
dropdownY = list()
dropdownBuffer = 30
for i in range(numDropdowns):
    dropdownY.append(dropdownHeight*i + dropdownBuffer*(i + 3))
genreDropdown = dropdown.DropDown(
    [button_dark, button_light],
    [utl.COLORSCHEME[h.Scheme("BUTTON_NO_HOVER")], utl.COLORSCHEME[h.Scheme("BUTTON_HOVER")]],
    utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")],
    dropdownX, dropdownY[0], dropdownWidth, dropdownHeight, 
    pygame.font.SysFont('Verdana', utl.FONT_SIZE_SMALL), 
    "Select Genre:", ["Fiction", "History"])
languageDropdown = dropdown.DropDown(
    [button_dark, button_light],
    [utl.COLORSCHEME[h.Scheme("BUTTON_NO_HOVER")], utl.COLORSCHEME[h.Scheme("BUTTON_HOVER")]],
    utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")],
    dropdownX, dropdownY[1], dropdownWidth, dropdownHeight, 
    pygame.font.SysFont('Verdana', utl.FONT_SIZE_SMALL), 
    "Select Language:", ["English", "Spanish"])


''''''''''''''''''
'                '
' INPUTBOX STUFF  '
'                '
''''''''''''''''''
inputboxX = 375
inputboxWidth = 715
inputboxHeight = 50
inputboxY = 637
inputboxnBuffer = 30

inputBox = inputbox.InputBox(
    utl.COLORSCHEME[h.Scheme("OUTLINE_HOVER")],
    utl.COLORSCHEME[h.Scheme("OUTLINE_NO_HOVER")],
    utl.COLORSCHEME[h.Scheme("TEXT_HOVER")],
    inputboxX,
    inputboxY,
    inputboxWidth,
    inputboxHeight,
    pygame.font.SysFont('Verdana', utl.FONT_SIZE_SMALL))
''''''''''''''''''
'                '
'  MAIN FUNCTION '
'                '
''''''''''''''''''
def updateMain(event_list: list):
    # Create screen swap button text, outline, filling, and hovering variables
    sideBarLWidth = 360
    button_h = text_button_dark.get_height()
    button_w = text_button_dark.get_width()
    offset_h = text_button_dark.get_height()//5
    offset_w = text_button_dark.get_width()//2
    midButtonW = utl.WINDOW_WIDTH/2 - button_w/2 + sideBarLWidth/2
    midButtonH = utl.WINDOW_HEIGHT/2 - button_h/2
    buttonLocX = midButtonW - offset_w/2
    buttonLocY = midButtonH - offset_h/2
    buttonWithOffsetW = button_w + offset_w
    buttonWithOffsetH = button_h + offset_h
    # Rectangle for quit button
    viewStoryButtonRect = pygame.Rect(buttonLocX, buttonLocY, buttonWithOffsetW, buttonWithOffsetH)

    # Fill MAIN_MENU_WINDOW background gradient and get mouse position
    startColor = ImageColor.getcolor(utl.COLORSCHEME[h.Scheme("BACKGROUND")], "RGB")
    endColor = ImageColor.getcolor(utl.COLORSCHEME[h.Scheme("BACKGROUND2")], "RGB")
    gradient.fillGradient(utl.MAIN_MENU_WINDOW, startColor, endColor)
    h.drawBorder(utl.MAIN_MENU_WINDOW)
    
    # utl.MAIN_MENU_WINDOW.fill(utl.COLORSCHEME[h.Scheme("BACKGROUND")])
    mouse = pygame.mouse.get_pos()
    
    # View story button interior (hover or no hover)
    if viewStoryButtonRect.collidepoint(mouse):
        pygame.draw.rect(utl.MAIN_MENU_WINDOW, button_light, viewStoryButtonRect, border_radius=3)
        utl.MAIN_MENU_WINDOW.blit(text_button_light, text_button_light.get_rect(center = viewStoryButtonRect.center))
    else:
        pygame.draw.rect(utl.MAIN_MENU_WINDOW, button_dark, viewStoryButtonRect, border_radius=3)
        utl.MAIN_MENU_WINDOW.blit(text_button_dark, text_button_dark.get_rect(center = viewStoryButtonRect.center))
        
    # View story button outline
    pygame.draw.rect(utl.MAIN_MENU_WINDOW, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")], viewStoryButtonRect, 2, 3)
    
    # Main menu text message
    mainMenuTextLocX = utl.WINDOW_WIDTH/2 - text_main_menu.get_width()/2 + sideBarLWidth/2
    mainMenuTextLocY = utl.WINDOW_HEIGHT/2 - text_main_menu.get_height()/2-100
    utl.MAIN_MENU_WINDOW.blit(text_main_menu, (mainMenuTextLocX, mainMenuTextLocY))
    
    # Update dropdowns
    selected_option_genre = genreDropdown.update(event_list)
    selected_option_language = languageDropdown.update(event_list)
    if selected_option_genre >= 0:
        genreDropdown.main = genreDropdown.options[selected_option_genre]
    elif selected_option_language >= 0:
        languageDropdown.main = languageDropdown.options[selected_option_language]
        
    # Draw vertical dropdown separator
    utl.MAIN_MENU_WINDOW.blit(text_select_menu, (dropdownX, dropdownHeight/2))
    pygame.draw.line(utl.MAIN_MENU_WINDOW, utl.COLORSCHEME[h.Scheme("TEXT_NO_HOVER")], (sideBarLWidth, 10), (sideBarLWidth, 690), width=2)
    genreDropdown.draw(utl.MAIN_MENU_WINDOW)
    languageDropdown.draw(utl.MAIN_MENU_WINDOW)
    Genre = genreDropdown.current_value
    Language = languageDropdown.current_value

    #add textbox
    inputBox.draw(utl.MAIN_MENU_WINDOW)
    text = ""
    if len(event_list) > 0:
        text = inputBox.update(event_list[0])
        
    
    return viewStoryButtonRect, Genre, Language
