import pygame as pg
import time
import requests
import utility as utl

class Chat():
    def __init__(self, color_inactive, color_font, x, y, w, h, font, text=''):
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
        
         
    def draw(self, surf):
        pg.draw.rect(surf, self.color_inactive, self.rect, 2, border_radius=3)
        rect = self.rect
        y = rect.top
        lineSpacing = -2
        fontHeight = self.font.size("Tg")[1]

        text = self.text
        while text:
            i = 1
            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break
            # determine maximum width of line
            while self.font.size(text[:i])[0] < rect.width - 5 and i < len(text):
                i += 1
            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1
            surf.blit(self.font.render(text[:i], True, self.color_font), (rect.left + 5, y + 5))
            y += fontHeight + lineSpacing
            # remove the text we just blitted
            text = text[i:]
        

    def update(self, events, text, isMsg, new_color_inactive, new_color_font, new_font):
        self.color_inactive = new_color_inactive
        self.color_font = new_color_font
        self.font = new_font
        import utility as utl

   
        if isMsg:
            r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender":  utl.session_id, "message": text})
            for i in r.json():
                bot_message = i['text']
                self.text = text + " response: " + bot_message 

            #self.text = text
        self.txt_surface = self.font.render(self.text, True, self.color_font)