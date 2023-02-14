import pygame
# import dropdown
import sounds
import utility as utl
import helpers as h
import main
import story
pygame.init()
pygame.font.init()

def run():
    in_main_window = True
    
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        event_list = pygame.event.get()
        if in_main_window:
            viewStoryButtonRect, genre, language = main.updateMain(event_list)
            utl.Genre = genre
            utl.Language = language
        else:
            backToMenuButtonRect = story.updateStory(event_list)
        
        # Check for any button pushes or program closure
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if in_main_window and viewStoryButtonRect.collidepoint(mouse):
                    sounds.playSound("success")
                    in_main_window = False
                elif not in_main_window and backToMenuButtonRect.collidepoint(mouse):
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

#Change the "1" argument in the line below to "2" to try the second color scheme from "Colorschemes.txt".
#You will need both line 152 and 153 un-commented in order to test the color schemes in "Colorschemes.txt".

#Un-comment the line below to change color schemes
utl.COLORSCHEME = h.applyColorScheme(utl.MAIN_COLOR_SCHEME)
run()
