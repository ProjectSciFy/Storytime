import pygame as pg
import time

class InputBox():
    
    def __init__(self, color_active, color_inactive, color_font, x, y, w, h, font, text=''):
        self.color_active = color_active
        self.color = self.color_active
        self.color_inactive = color_inactive
        self.color_font = color_font
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.txt_surface = font.render(text, True, self.color_font)
        self.font = font
        self.active = False
        self.cursor = pg.Rect(self.txt_surface.get_rect().topright, (3, self.txt_surface.get_rect().height + 2))

        
    def draw(self, surf):
        # Blit the text.
        surf.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(surf, self.color_inactive, self.rect, 2, border_radius=3)

        if self.active:
            pg.draw.rect(surf, self.color_active, self.rect, 2, border_radius=3)
            if time.time() % 1 > 0.5:
                # set cursor position
                self.cursor.midleft = (self.rect.midleft[0] + self.txt_surface.get_rect().width + 1, self.rect.midleft[1])

                pg.draw.rect(surf, self.color, self.cursor)

    def update(self, event):
        text = self.text
        if event.type == pg.MOUSEBUTTONDOWN:
         # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    text = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

        return text
