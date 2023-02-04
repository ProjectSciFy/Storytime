import pygame
pygame.init()

res = (1100, 700)

screen = pygame.display.set_mode(res)


'''
BUTTON STUFF:
'''
# light shade of the button
color_light = ('#CEDED5')
# dark shade of the button
color_dark = ('#B6CEC1')

width = screen.get_width()
height = screen.get_height()
  
# defining a font
smallfont = pygame.font.SysFont('Arial',35)
  
text_button = smallfont.render('Quit' , True , '#72705B')
text_button_light = smallfont.render('Quit' , True , '#A4A28E')
text_main_menu = smallfont.render('Welcome to Storytime!' , True , '#72705B')

while True:
    button_l = 40
    button_w = 140
    offset_l = 0
    offset_w = text_button.get_width()/2 + text_button.get_width()/10

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if the mouse is clicked on the
            # button the game is terminated
            if width/2-button_w/2<= mouse[0] <= width/2+button_w/2 and height/2-button_l/2 <= mouse[1] <= height/2+button_l/2:
                pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill('#D5ECDC')
    mouse = pygame.mouse.get_pos()
    
    if width/2-button_w/2<= mouse[0] <= width/2+button_w/2 and height/2-button_l/2 <= mouse[1] <= height/2+button_l/2:
        pygame.draw.rect(screen,color_light,[width/2-button_w/2,height/2-button_l/2,button_w,button_l],border_radius=3)
        pygame.draw.rect(screen,'#72705B',[width/2-button_w/2,height/2-button_l/2,button_w,button_l],2,3)
        screen.blit(text_button_light, (width/2-button_w/2+offset_w,height/2-button_l/2+offset_l))
    else:
        pygame.draw.rect(screen,color_dark,[width/2-button_w/2,height/2-button_l/2,button_w,button_l],border_radius=3)
        pygame.draw.rect(screen,'#72705B',[width/2-button_w/2,height/2-button_l/2,button_w,button_l],2,3)
        screen.blit(text_button, (width/2-button_w/2+offset_w,height/2-button_l/2+offset_l))
      
    screen.blit(text_main_menu, (width/2-text_main_menu.get_width()/2,height/2-text_main_menu.get_height()/2-100))
    
    pygame.display.update()