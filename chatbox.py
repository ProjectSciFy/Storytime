import pygame as pg
import time
import utility as utl
import helpers as h

class ChatBox():
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
        self.display_text = text
        self.txt_surface = font.render(text, True, self.color_font)
        self.font = font
        self.active = False
        self.cursor = pg.Rect(self.txt_surface.get_rect().topright, (3, self.txt_surface.get_rect().height + 2))

    def draw(self, surf):
        # Blit the rect.
        pg.draw.rect(surf, self.color_inactive, self.rect, 2, border_radius=3)

        # Render the full text
        full_text_surface = self.font.render(self.text, True, self.color_font)
        
        # Calculate the size of the full text
        full_text_rect = full_text_surface.get_rect()
        
        # Calculate the start index of the displayed text
        start_index = max(full_text_rect.width - self.w + 10, 0)

        # Create a new surface to hold the clipped text
        clipped_text_surface = pg.Surface((self.w - 10, self.h - 18), pg.SRCALPHA)
        clipped_text_surface.fill((255, 255, 255, 0))
        
        # Blit the clipped section of the full text onto the new surface
        clipped_text_surface.blit(full_text_surface, (0, 0), (start_index, 0, self.w - 10, self.h - 6))
        
        # Blit the clipped text surface onto the chat box
        surf.blit(clipped_text_surface, (self.x + 5, self.y + 9))
        
        # Render the cursor
        if self.active:
            pg.draw.rect(surf, self.color_active, self.rect, 2, border_radius=3)
            if time.time() % 1 > 0.5:
                cursor_pos = self.rect.x + 5 + full_text_surface.get_rect().width
                if cursor_pos > (self.rect.x + 5 + clipped_text_surface.get_rect().width):
                    cursor_pos = self.rect.x + 5 + clipped_text_surface.get_rect().width
                self.cursor.midleft = (cursor_pos, self.rect.midleft[1])
                pg.draw.rect(surf, self.color_font, self.cursor)

    def update(self, events, new_color_active, new_color_inactive, new_color_font, new_font):
        self.color_active = new_color_active
        self.color_inactive = new_color_inactive
        self.color_font = new_color_font
        self.font = new_font
        text = self.text
        isMsg = False
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
            if event.type == pg.KEYDOWN:
                if self.active:
                    if event.key == pg.K_RETURN:
                        text = self.text
                        self.text = ''
                        isMsg = True
                    elif event.key == pg.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
        self.txt_surface = self.font.render(self.text, True, self.color)

        return text, isMsg