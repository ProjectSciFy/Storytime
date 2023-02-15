import pygame as pg
import sounds

class DropDown():
    
    def __init__(self, color_menu, color_option, color_font, x, y, w, h, font, main, options):
        self.color_menu = color_menu
        self.color_option = color_option
        self.color_font = color_font
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = font
        self.main = main
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1
        self.current_value = ""

    def draw(self, surf):
        startTop = (self.rect.midright[0] - 30, self.rect.midright[1] - self.rect.size[1]//4)
        startBot = (self.rect.midright[0] - 30, self.rect.midright[1] + self.rect.size[1]//4)
        end = (self.rect.midright[0] - 10, self.rect.midright[1])
        pg.draw.rect(surf, self.color_menu[self.menu_active], self.rect, border_radius=3)
        pg.draw.line(surf, self.color_font, startTop, end, width=3)
        pg.draw.line(surf, self.color_font, startBot, end, width=3)
        pg.draw.rect(surf, self.color_font, self.rect, 2, 3)
        self.font.set_italic(True)
        msg = self.font.render(self.main, 1, self.color_font)
        self.font.set_italic(False)
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            pg.draw.line(surf, self.color_font, startTop, end, width=5)
            pg.draw.line(surf, self.color_font, startBot, end, width=5)
            pg.draw.rect(surf, self.color_font, self.rect, 3, 3)
            self.font.set_italic(True)
            self.font.set_bold(True)
            surf.blit(msg, msg.get_rect(center = self.rect.center))
            self.font.set_italic(False)
            self.font.set_bold(False)
            for i, text in enumerate(self.options):
                rect = pg.Rect(self.x + self.rect.size[0], self.y, self.w, self.h)
                rect.y += (i) * self.rect.height
                pg.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, border_radius=3)
                pg.draw.rect(surf, self.color_font, rect, 2, 3)
                msg = self.font.render(text, 1, self.color_font)
                surf.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list):
        mpos = pg.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.options)):
            rect = pg.Rect(self.x + self.rect.size[0], self.y, self.w, self.h)
            rect.y += (i) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                self.current_value = self.options[self.active_option]
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    sounds.playSound('cling')
                    self.draw_menu = False
                    return self.active_option
        return -1
