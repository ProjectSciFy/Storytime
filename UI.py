import pygame
import dropdown
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
STORY_WINDOW = pygame.display.set_mode(RESOLUTION)
MAIN_MENU_WINDOW = pygame.display.set_mode(RESOLUTION)
in_main_window = True
FONT_SIZE = 30
FONT_SIZE_SMALL = 24
FONT = pygame.font.SysFont('Verdana',FONT_SIZE)
SMALL_FONT = pygame.font.SysFont('Verdana',FONT_SIZE_SMALL)
BUTTON_EXPAND_BUFFER = 5
MAIN_COLOR_SCHEME = 5
Genre = ""
Length = ""
Language = ""
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
        locx = 320
        locy = -60
        size = 50
        offset = 5
        schemNum = 1
        # Print squares of each color scheme
        for scheme in colorschemes:
            text_button = FONT.render(f"Color Scheme #{schemNum}:" , True, "#ffffff")
            locx = 320
            locy += y_offset
            MAIN_MENU_WINDOW.blit(text_button, (x_offset + offset, locy + offset))
            for color in scheme:
                x = locx
                y = locy
                pygame.draw.rect(MAIN_MENU_WINDOW, color, pygame.Rect(x, y, 60, 60), border_radius=3)
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

def run():
    in_main_window = True
    # Grab colors from color scheme
    button_light = COLORSCHEME[Scheme("BUTTON_HOVER")]
    button_dark = COLORSCHEME[Scheme("BUTTON_NO_HOVER")]
    # Render colors, text, and font for screen swap button (hover/no hover) and main menu text message
    text_button_dark = FONT.render('View Story' , True , COLORSCHEME[Scheme("TEXT_NO_HOVER")])
    text_button_light = FONT.render('View Story' , True , COLORSCHEME[Scheme("TEXT_HOVER")])
    text_button_dark_back_main = FONT.render('Go to Main Menu' , True , COLORSCHEME[Scheme("TEXT_NO_HOVER")])
    text_button_light_back_main = FONT.render('Go to Main Menu' , True , COLORSCHEME[Scheme("TEXT_HOVER")])
    FONT.set_bold(True)
    FONT.set_underline(True)
    text_main_menu = FONT.render('Welcome to Storytime!' , True , COLORSCHEME[Scheme("TEXT_NO_HOVER")])
    text_select_menu = FONT.render('Customize Story:' , True , COLORSCHEME[Scheme("TEXT_NO_HOVER")])
    text_story = FONT.render('Story Time!' , True , COLORSCHEME[Scheme("TEXT_NO_HOVER")])
    FONT.set_bold(False)
    FONT.set_underline(False)
    # Dropdowns setup
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
        [COLORSCHEME[Scheme("BUTTON_NO_HOVER")], COLORSCHEME[Scheme("BUTTON_HOVER")]],
        COLORSCHEME[Scheme("TEXT_NO_HOVER")],
        dropdownX, dropdownY[0], dropdownWidth, dropdownHeight, 
        pygame.font.SysFont('Verdana', FONT_SIZE_SMALL), 
        "Select Genre:", ["Fiction", "History"])
    languageDropdown = dropdown.DropDown(
        [button_dark, button_light],
        [COLORSCHEME[Scheme("BUTTON_NO_HOVER")], COLORSCHEME[Scheme("BUTTON_HOVER")]],
        COLORSCHEME[Scheme("TEXT_NO_HOVER")],
        dropdownX, dropdownY[1], dropdownWidth, dropdownHeight, 
        pygame.font.SysFont('Verdana', FONT_SIZE_SMALL), 
        "Select Language:", ["English", "Spanish"])
    running = True
    while running:
        # Events:
        event_list = pygame.event.get()
        if in_main_window:
            # Create screen swap button text, outline, filling, and hovering variables
            sideBarLWidth = 360
            button_h = text_button_dark.get_height()
            button_w = text_button_dark.get_width()
            offset_h = text_button_dark.get_height()//5
            offset_w = text_button_dark.get_width()//2
            midButtonW = WINDOW_WIDTH/2 - button_w/2 + sideBarLWidth/2
            midButtonH = WINDOW_HEIGHT/2 - button_h/2
            buttonLocX = midButtonW - offset_w/2
            buttonLocY = midButtonH - offset_h/2
            buttonWithOffsetW = button_w + offset_w
            buttonWithOffsetH = button_h + offset_h
            # Rectangle for quit button
            viewStoryButtonRect = pygame.Rect(buttonLocX, buttonLocY, buttonWithOffsetW, buttonWithOffsetH)

            # Fill MAIN_MENU_WINDOW background and get mouse position
            MAIN_MENU_WINDOW.fill(COLORSCHEME[Scheme("BACKGROUND")])
            mouse = pygame.mouse.get_pos()
            
            # View story button interior (hover or no hover)
            if viewStoryButtonRect.collidepoint(mouse):
                pygame.draw.rect(MAIN_MENU_WINDOW, button_light, viewStoryButtonRect, border_radius=3)
                MAIN_MENU_WINDOW.blit(text_button_light, text_button_light.get_rect(center = viewStoryButtonRect.center))
            else:
                pygame.draw.rect(MAIN_MENU_WINDOW, button_dark, viewStoryButtonRect, border_radius=3)
                MAIN_MENU_WINDOW.blit(text_button_dark, text_button_dark.get_rect(center = viewStoryButtonRect.center))
                
            # View story button outline
            pygame.draw.rect(MAIN_MENU_WINDOW, COLORSCHEME[Scheme("TEXT_NO_HOVER")], viewStoryButtonRect, 2, 3)
            
            # Main menu text message
            mainMenuTextLocX = WINDOW_WIDTH/2 - text_main_menu.get_width()/2 + sideBarLWidth/2
            mainMenuTextLocY = WINDOW_HEIGHT/2 - text_main_menu.get_height()/2-100
            MAIN_MENU_WINDOW.blit(text_main_menu, (mainMenuTextLocX, mainMenuTextLocY))
            
            # Update dropdowns
            selected_option_genre = genreDropdown.update(event_list)
            selected_option_language = languageDropdown.update(event_list)
            if selected_option_genre >= 0:
                genreDropdown.main = genreDropdown.options[selected_option_genre]
            elif selected_option_language >= 0:
                languageDropdown.main = languageDropdown.options[selected_option_language]
            # Draw vertical dropdown separator
            MAIN_MENU_WINDOW.blit(text_select_menu, (dropdownX, dropdownHeight/2))
            pygame.draw.line(MAIN_MENU_WINDOW, COLORSCHEME[Scheme("TEXT_NO_HOVER")], (sideBarLWidth, 10), (sideBarLWidth, 690), width=2)
            genreDropdown.draw(MAIN_MENU_WINDOW)
            languageDropdown.draw(MAIN_MENU_WINDOW)
            Genre = genreDropdown.current_value
            Language = languageDropdown.current_value
        else:
            # Create screen swap button text, outline, filling, and hovering variables
            sideBarLWidth = 0
            button_h = text_button_dark_back_main.get_height()
            button_w = text_button_dark_back_main.get_width()
            offset_h = text_button_dark_back_main.get_height()//5
            offset_w = text_button_dark_back_main.get_width()//2
            midButtonW = WINDOW_WIDTH/2 - button_w/2 + sideBarLWidth/2
            midButtonH = WINDOW_HEIGHT/2 - button_h/2
            buttonLocX = midButtonW - offset_w/2
            buttonLocY = midButtonH - offset_h/2
            buttonWithOffsetW = button_w + offset_w
            buttonWithOffsetH = button_h + offset_h
            # Rectangle for back to main menu button
            backToMenuButtonRect = pygame.Rect(buttonLocX, buttonLocY, buttonWithOffsetW, buttonWithOffsetH)

            # Fill STORY_WINDOW background and get mouse position
            STORY_WINDOW.fill(COLORSCHEME[Scheme("BACKGROUND")])
            mouse = pygame.mouse.get_pos()
            
            # Back to main menu button interior (hover or no hover)
            if backToMenuButtonRect.collidepoint(mouse):
                pygame.draw.rect(STORY_WINDOW, button_light, backToMenuButtonRect, border_radius=3)
                STORY_WINDOW.blit(text_button_light_back_main, text_button_light_back_main.get_rect(center = backToMenuButtonRect.center))
            else:
                pygame.draw.rect(STORY_WINDOW, button_dark, backToMenuButtonRect, border_radius=3)
                STORY_WINDOW.blit(text_button_dark_back_main, text_button_dark_back_main.get_rect(center = backToMenuButtonRect.center))
                
            # Back to main menu story button outline
            pygame.draw.rect(STORY_WINDOW, COLORSCHEME[Scheme("TEXT_NO_HOVER")], backToMenuButtonRect, 2, 3)
            
            # Story time text message
            storyTextLocX = WINDOW_WIDTH/2 - text_story.get_width()/2 + sideBarLWidth/2
            storyTextLocY = WINDOW_HEIGHT/2 - text_story.get_height()/2-100
            STORY_WINDOW.blit(text_story, (storyTextLocX, storyTextLocY))
        
        # Check for any button pushes or program closure
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if in_main_window and viewStoryButtonRect.collidepoint(mouse):
                    in_main_window = False
                elif not in_main_window and backToMenuButtonRect.collidepoint(mouse):
                    in_main_window = True
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
    pygame.quit()
''''''''''''''''''''''''''''''''''''
        
#If you uncomment this line, you must comment out all lines below this function (they will be unreachable.)

# Un-comment the line below to see all color schemes in "Colorschemes.txt".
# displaySchemes()

''''''''''''''''''''''''''''''''''''

#Change the "1" argument in the line below to "2" to try the second color scheme from "Colorschemes.txt".
#You will need both line 152 and 153 un-commented in order to test the color schemes in "Colorschemes.txt".

#Un-comment the line below to change color schemes
COLORSCHEME = applyColorScheme(MAIN_COLOR_SCHEME)
run()
