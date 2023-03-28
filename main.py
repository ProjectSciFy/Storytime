import pygame
from PIL import ImageColor
import utility as utl
import helpers as h
import dropdown
import gradient
import chatbox
import chat


''''''''''''''''''
'                '
' CREATE OBJECTS '
'                '
''''''''''''''''''
# Grab colors from color scheme
button_light = utl.colorscheme[h.Scheme("BUTTON_HOVER")]
button_dark = utl.colorscheme[h.Scheme("BUTTON_NO_HOVER")]
# Render colors, text, and font for screen swap button (hover/no hover) and main menu text message
text_button_dark = utl.SysFont.render('View Story' , True , utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
text_button_light = utl.SysFont.render('View Story' , True , utl.colorscheme[h.Scheme("TEXT_HOVER")])
utl.SysFont.set_bold(True)
text_select_menu = utl.SysFont.render('Customize Story:' , True , utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
utl.SysFont.set_bold(False)
''''''''''''''''''
'                '
' DROPDOWN STUFF '
'                '
''''''''''''''''''
numDropdowns = 3
dropdownX = 30
dropdownWidth = 300
dropdownHeight = 50
dropdownY = list()
dropdownBuffer = 30
for i in range(numDropdowns):
    dropdownY.append(dropdownHeight*i + dropdownBuffer*(i + 3))
colorDropdown = dropdown.DropDown(
    [button_dark, button_light],
    [utl.colorscheme[h.Scheme("BUTTON_NO_HOVER")], utl.colorscheme[h.Scheme("BUTTON_HOVER")]],
    [utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], utl.colorscheme[h.Scheme("TEXT_HOVER")]],
    dropdownX, dropdownY[0], dropdownWidth, dropdownHeight, 
    pygame.font.SysFont(utl.Font, utl.font_size_small), 
    "Color Scheme:", ["Original", "Forest", "Mountain", "Fire"], "color")
fontDropdown = dropdown.DropDown(
    [button_dark, button_light],
    [utl.colorscheme[h.Scheme("BUTTON_NO_HOVER")], utl.colorscheme[h.Scheme("BUTTON_HOVER")]],
    [utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], utl.colorscheme[h.Scheme("TEXT_HOVER")]],
    dropdownX, dropdownY[1], dropdownWidth, dropdownHeight, 
    pygame.font.SysFont(utl.Font, utl.font_size_small), 
    "Font:", ["Verdana", "Gillsans", "Comic Sans", "Kannadamn"], "font")
soundDropdown = dropdown.DropDown(
    [button_dark, button_light],
    [utl.colorscheme[h.Scheme("BUTTON_NO_HOVER")], utl.colorscheme[h.Scheme("BUTTON_HOVER")]],
    [utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], utl.colorscheme[h.Scheme("TEXT_HOVER")]],
    dropdownX, dropdownY[2], dropdownWidth, dropdownHeight, 
    pygame.font.SysFont(utl.Font, utl.font_size_small), 
    "Sound:", ["Enable", "Disable"], "sound")

''''''''''''''''''
'                '
' INPUTBOX STUFF '
'                '
''''''''''''''''''
inputboxX = 392
inputboxWidth = 679
inputboxHeight = 50
inputboxY = 637
inputboxnBuffer = 30

chatBox = chatbox.ChatBox(
    utl.colorscheme[h.Scheme("OUTLINE_HOVER")],
    utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")],
    utl.colorscheme[h.Scheme("TEXT_HOVER")],
    inputboxX,
    inputboxY,
    inputboxWidth,
    inputboxHeight,
    pygame.font.SysFont(utl.Font, utl.font_size_small))
msg = ""

''''''''''''''''''
'                '
'   CHAT STUFF   '
'                '
''''''''''''''''''
chatX = 392
chatY = 30
chatWidth = 679
chatHeight = 582
chatWindow = chat.Chat(
    utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")],
    utl.colorscheme[h.Scheme("TEXT_NO_HOVER")],
    chatX,
    chatY,
    chatWidth,
    chatHeight,
    pygame.font.SysFont(utl.Font, utl.font_size_small))

''''''''''''''''''
'                '
'  MAIN FUNCTION '
'                '
''''''''''''''''''
def updateMain(event_list: list):
    # Grab colors from color scheme
    button_light = utl.colorscheme[h.Scheme("BUTTON_HOVER")]
    button_dark = utl.colorscheme[h.Scheme("BUTTON_NO_HOVER")]
    # Render colors, text, and font for screen swap button (hover/no hover) and main menu text message
    text_button_dark = utl.SysFont.render('View Story' , True , utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
    text_button_light = utl.SysFont.render('View Story' , True , utl.colorscheme[h.Scheme("TEXT_HOVER")])
    utl.SysFont.set_bold(True)
    text_select_menu = utl.SysFont.render('Customize Story:' , True , utl.colorscheme[h.Scheme("TEXT_NO_HOVER")])
    utl.SysFont.set_bold(False)
    
    # Create screen swap button text, outline, filling, and hovering variables
    sideBarLWidth = 360
    buttonLocX = dropdownX
    buttonLocY = 637
    buttonWithOffsetW = 300
    buttonWithOffsetH = 50
    viewStoryButtonRect = pygame.Rect(buttonLocX, buttonLocY, buttonWithOffsetW, buttonWithOffsetH)

    # Fill MAIN_MENU_WINDOW background gradient and get mouse position
    startColor = ImageColor.getcolor(utl.colorscheme[h.Scheme("BACKGROUND")], "RGB")
    endColor = ImageColor.getcolor(utl.colorscheme[h.Scheme("BACKGROUND2")], "RGB")
    gradient.fillGradient(utl.MAIN_MENU_WINDOW, startColor, endColor)
    h.drawBorder(utl.MAIN_MENU_WINDOW)
    
    # utl.MAIN_MENU_WINDOW.fill(utl.colorscheme[h.Scheme("BACKGROUND")])
    mouse = pygame.mouse.get_pos()
    
    # View story button interior (hover or no hover)
    if viewStoryButtonRect.collidepoint(mouse):
        pygame.draw.rect(utl.MAIN_MENU_WINDOW, button_light, viewStoryButtonRect, border_radius=3)
        utl.MAIN_MENU_WINDOW.blit(text_button_light, text_button_light.get_rect(center = viewStoryButtonRect.center))
        pygame.draw.rect(utl.MAIN_MENU_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_HOVER")], viewStoryButtonRect, 2, 3)
    else:
        pygame.draw.rect(utl.MAIN_MENU_WINDOW, button_dark, viewStoryButtonRect, border_radius=3)
        utl.MAIN_MENU_WINDOW.blit(text_button_dark, text_button_dark.get_rect(center = viewStoryButtonRect.center))
        pygame.draw.rect(utl.MAIN_MENU_WINDOW, utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")], viewStoryButtonRect, 2, 3)
    
    # Add textbox
    text, isMsg = chatBox.update(event_list, utl.colorscheme[h.Scheme("OUTLINE_HOVER")], utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")], utl.colorscheme[h.Scheme("TEXT_HOVER")], utl.SysSmallFont)
    chatWindow.update(event_list, text, isMsg, utl.colorscheme[h.Scheme("OUTLINE_NO_HOVER")], utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], utl.SysSmallFont) 
    chatBox.draw(utl.MAIN_MENU_WINDOW)
    chatWindow.draw(utl.MAIN_MENU_WINDOW)
    
    # Update dropdowns
    selected_option_color = colorDropdown.update(event_list)
    selected_option_font = fontDropdown.update(event_list)
    selected_option_sound = soundDropdown.update(event_list)
    if selected_option_color >= 0:
        colorDropdown.main = colorDropdown.options[selected_option_color]
    elif selected_option_font >= 0:
        fontDropdown.main = fontDropdown.options[selected_option_font]
    elif selected_option_sound >= 0:
        soundDropdown.main = soundDropdown.options[selected_option_sound]
        
    # Draw vertical dropdown separator
    utl.MAIN_MENU_WINDOW.blit(text_select_menu, (dropdownX, dropdownHeight/2))
    pygame.draw.line(utl.MAIN_MENU_WINDOW, utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], (sideBarLWidth, 10), (sideBarLWidth, 690), width=2)
    colorDropdown.draw(utl.MAIN_MENU_WINDOW)
    fontDropdown.draw(utl.MAIN_MENU_WINDOW)
    soundDropdown.draw(utl.MAIN_MENU_WINDOW)
    
    return viewStoryButtonRect
