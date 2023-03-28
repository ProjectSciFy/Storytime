import pygame
import sounds
import utility as utl
import helpers as h
pygame.init()
utl.MAIN_COLOR_SCHEME = 1
utl.colorscheme = h.applyColorScheme(utl.MAIN_COLOR_SCHEME)   

def run(): 
    import main
    import story
    
    in_main_window = True
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        event_list = pygame.event.get()
        if in_main_window:
            viewStoryButtonRect = main.updateMain(event_list)
        else:
            backToMenuButtonRect = story.updateStory(event_list)
        
        # Check for any button pushes or program closure
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if in_main_window and viewStoryButtonRect.collidepoint(mouse):
                    if utl.Sound.upper() == "ENABLE":
                        sounds.playSound("success")
                    in_main_window = False
                elif not in_main_window and backToMenuButtonRect.collidepoint(mouse):
                    if utl.Sound.upper() == "ENABLE":
                        sounds.playSound("success")
                    in_main_window = True
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
    pygame.quit()
    
    
''''''''''''''''''''''''''''''''''''
        
#If you uncomment this line, you must comment out all lines below this function (they will be unreachable.)

# Un-comment the line below to see all color schemes in "Colorschemes.txt".
# h.displaySchemes()

''''''''''''''''''''''''''''''''''''

import fadeIn as fi
fi.fadeInText()
run()
