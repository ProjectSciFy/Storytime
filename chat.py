import pygame as pg
import requests
import utility as utl
import helpers as h

class Chat():
    def __init__(self, color_inactive, color_font, x, y, w, h, font):
        self.allHistory = []
        self.isRASA = []
        self.color_inactive = color_inactive
        self.color_font = color_font
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = font
        self.active = False
        self.linespacing = -2
        self.scroll_pos = 0
        self.max_height = 572
        self.font_height = self.font.size("Tg")[1]
        self.num_messages = len(self.allHistory)
        self.line_height = self.font_height + self.linespacing
        self.max_messages = self.max_height // self.line_height
        # Determine the first and last messages to display based on the scroll position
        self.first_msg_index = max(self.num_messages - self.scroll_pos - self.max_messages, 0)
        self.last_msg_index = max(self.num_messages - self.scroll_pos, 0)

        self.send_chatbot("hi")

    def draw(self, surf):
        pg.draw.rect(surf, self.color_inactive, self.rect, 2, border_radius=3)
        rect = self.rect
        for i in range(self.first_msg_index, self.last_msg_index):
            lines = self.wrap_text(self.allHistory[(self.last_msg_index - (i - self.first_msg_index) - 1)], self.font, self.w - 5)
            num_lines = len(lines)
            for j, line in enumerate(lines):
                txt_surface = self.font.render(line, True, self.color_font)
                index = (self.last_msg_index - (i - self.first_msg_index) - 1) + j
                if self.isRASA[index] == True:
                    txt_surface = self.font.render(line, True, utl.colorscheme[h.Scheme("TEXT_RASA")])
                text_rect = txt_surface.get_rect()
                text_rect.x = rect.left + 5
                text_rect.y = rect.bottom - ((i - self.first_msg_index) * (num_lines * self.line_height)) - ((num_lines - j - 1) * self.line_height) - 5 - self.line_height * 0.5 - (self.font_height + self.linespacing)/2
                # Check if the text surface is above the chat box
                if text_rect.y + self.font_height < rect.top:
                    continue
                surf.blit(txt_surface, text_rect)

    def send_chatbot(self, text):
        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": utl.session_id, "message": text})
        bot_message = ""
        for i in r.json():
            bot_message = bot_message + i['text']
        bot_lines = self.wrap_text(bot_message, self.font, self.w - 5)
        for line in bot_lines:
            self.allHistory.append(line)
            self.isRASA.append(True)

    def update(self, events, text, isMsg, new_color_inactive, new_color_font, new_font):
        self.color_inactive = new_color_inactive
        self.color_font = new_color_font
        self.font = new_font
        self.font_height = self.font.size("Tg")[1]
        self.line_height = self.font_height + self.linespacing
        self.max_messages = self.max_height // self.line_height
        if isMsg and len(text) > 0:
            lines = self.wrap_text(text, self.font, self.w - 5)
            for line in lines:
                self.allHistory.append(line)
                self.isRASA.append(False)
            self.send_chatbot(text)
        self.num_messages = len(self.allHistory)
        # Determine the first and last messages to display based on the scroll position
        self.first_msg_index = max(self.num_messages - self.scroll_pos - self.max_messages, 0)
        self.last_msg_index = max(self.num_messages - self.scroll_pos, 0)
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and self.num_messages > self.max_messages:
                    if self.scroll_pos < self.num_messages - self.max_messages:
                        self.scroll_pos += 1
                elif event.key == pg.K_DOWN and self.num_messages > self.max_messages:
                    if self.scroll_pos > 0:
                        self.scroll_pos -= 1


    def wrap_text(self, text, font, max_width):
        ret = []
        if font.size(text)[0] < max_width:
            ret.append(text)
        else:
            words = text.split()
            current_line = words[0]
            for word in words[1:]:
                if font.size(current_line + ' ' + word)[0] < max_width:
                    current_line += ' ' + word
                else:
                    ret.append(current_line)
                    current_line = word
            ret.append(current_line)

        # Check if each line needs to be further broken up by character
        final_lines = []
        for line in ret:
            if font.size(line)[0] < max_width:
                final_lines.append(line)
            else:
                chars = []
                current_char = line[0]
                for char in line[1:]:
                    if font.size(current_char + char)[0] < max_width:
                        current_char += char
                    else:
                        chars.append(current_char)
                        current_char = char
                chars.append(current_char)
                final_lines.extend(chars)

        return final_lines

