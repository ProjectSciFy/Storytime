import pygame
import utility as utl

def fadeInText():
    image = pygame.image.load("story_time_logo.png").convert()
    image = pygame.transform.scale(image, (utl.WINDOW_WIDTH, utl.WINDOW_HEIGHT))
    window=pygame.display.set_mode((utl.WINDOW_WIDTH, utl.WINDOW_HEIGHT))
    background=pygame.Surface((window.get_rect().width, window.get_rect().height))


    for i in range (225):
        background.fill((0,0,0))    
        image.set_alpha(i)
        window.blit(image,(0,0))
        pygame.display.flip()
        pygame.time.delay(10)
    
    return 



# if __name__ == '__main__':
#     pygame.init()
#     fadeInText()


# def fadeInText():
#     screen = pygame.display.set_mode((utl.WINDOW_WIDTH, utl.WINDOW_HEIGHT))
#     FONT = pygame.font.SysFont('Verdana', 95)
#     text = FONT.render('Story Time !!!', False, pygame.Color(utl.COLORSCHEME[5]))
#     text_rect = text.get_rect(center=(utl.WINDOW_WIDTH/2, utl.WINDOW_HEIGHT/2))
#     surf = pygame.Surface(text.get_rect().size)
#     surf.set_colorkey((1,1,1))
#     surf.fill((1,1,1))
#     surf.blit(text, (0, 0))
#     clock = pygame.time.Clock()
#     alpha = 0

#     done = False
#     i = 0
#     while not done:
#         clock.tick(120)
#         i += 1
#         if i >= 256:
#             done = True

#         alpha = (alpha + 1) % 256
#         surf.set_alpha(alpha)
        
#         screen.fill(pygame.Color(utl.COLORSCHEME[0]))
#         screen.blit(surf, text_rect)
#         clock.tick(120)
#         # print(alpha)
#         pygame.display.update()