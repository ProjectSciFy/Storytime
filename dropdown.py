import pygame as pg
import sounds
import helpers as h

class DropDown():
    
    def __init__(self, color_menu, color_option, color_font, x, y, w, h, font, main: str, options: list, intent: str):
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
        self.intent = intent.upper()

    def draw(self, surf: pg.Surface):
        startTop = (self.rect.midright[0] - 30, self.rect.midright[1] - self.rect.size[1]//4)
        startBot = (self.rect.midright[0] - 30, self.rect.midright[1] + self.rect.size[1]//4)
        end = (self.rect.midright[0] - 10, self.rect.midright[1])
        pg.draw.rect(surf, self.color_menu[self.menu_active], self.rect, border_radius=3)
        pg.draw.line(surf, self.color_font[self.menu_active], startTop, end, width=3)
        pg.draw.line(surf, self.color_font[self.menu_active], startBot, end, width=3)
        pg.draw.rect(surf, self.color_font[self.menu_active], self.rect, 2, 3)
        self.font.set_italic(True)
        msg = self.font.render(self.main, 1, self.color_font[self.menu_active])
        self.font.set_italic(False)
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            pg.draw.line(surf, self.color_font[1], startTop, end, width=5)
            pg.draw.line(surf, self.color_font[1], startBot, end, width=5)
            pg.draw.rect(surf, self.color_font[1], self.rect, 3, 3)
            self.font.set_italic(True)
            self.font.set_bold(True)
            surf.blit(msg, msg.get_rect(center = self.rect.center))
            self.font.set_italic(False)
            self.font.set_bold(False)
            for i, text in enumerate(self.options):
                rect = pg.Rect(self.x + self.rect.size[0], self.y, self.w, self.h)
                rect.y += (i) * self.rect.height
                pg.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, border_radius=3)
                pg.draw.rect(surf, self.color_font[1 if i == self.active_option else 0], rect, 2, 3)
                msg = self.font.render(text, 1, self.color_font[1 if i == self.active_option else 0])
                surf.blit(msg, msg.get_rect(center = rect.center))

    def update(self, event_list: list, fontSizeChange = 0):
        mpos = pg.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        import utility as utl
        self.color_menu = [utl.colorscheme[h.Scheme("BUTTON_NO_HOVER")], utl.colorscheme[h.Scheme("BUTTON_HOVER")]]
        self.color_option = [utl.colorscheme[h.Scheme("BUTTON_NO_HOVER")], utl.colorscheme[h.Scheme("BUTTON_HOVER")]]
        self.color_font = [utl.colorscheme[h.Scheme("TEXT_NO_HOVER")], utl.colorscheme[h.Scheme("TEXT_HOVER")]]
        self.font = utl.SysSmallFont
        
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
                    if utl.Sound.upper() == "ENABLE":
                        sounds.playSound('cling')
                    if self.intent.upper() == "COLOR":
                        scheme = h.updateScheme(self.current_value)
                    if self.intent.upper() == "FONT":
                        utl.sysFont, utl.sysSmallFont = h.updateFont(self.current_value)
                    if self.intent.upper() == "SOUND":
                        h.updateSound(self.current_value) # function returns sound updated value, can access via sound = ...
                    self.draw_menu = False
                    return self.active_option
        return -1