import pygame
import sounds
import utility as utl
import helpers as h
import json
import requests
import chat
pygame.init()
utl.MAIN_COLOR_SCHEME = 1
utl.colorscheme = h.applyColorScheme(utl.MAIN_COLOR_SCHEME)   

with open('rasa/rasa_pass.json','r+') as f1:
    f1.seek(0)
    with open('default_config.json','r') as f2:
            data = json.load(f2)
    json.dump(data, f1, indent=4)
    f1.truncate()

def run(): 
    import main
    import story
    
    in_main_window = True
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        event_list = pygame.event.get()

        with open('rasa/rasa_pass.json','r') as f:
            data = json.load(f)
            utl.Scheme = data['scheme']
            utl.Font = data['font']
            utl.Sound = data['sound']
            utl.storyText = data['story']
            storyNumber = data['story_num']
            image_paths = data['image_paths']
            
        numOfEntries = len(utl.storyText)
        utl.storyImages = [pygame.transform.scale(pygame.image.load(f"./rasa/images/story_{storyNumber}/sentence_{i}.png"), (508, 508)) for i in range(numOfEntries)]

        h.updateScheme(utl.Scheme)
        utl.colorscheme = h.applyColorScheme(utl.MAIN_COLOR_SCHEME)   
        h.updateFont(utl.Font)
        h.updateSound(utl.Sound)


        if in_main_window:
            viewStoryButtonRect = main.updateMain(event_list)
        else:
            backToMenuButtonRect = story.updateStory(event_list)
        

        # Check for any button pushes or program closure
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if in_main_window and viewStoryButtonRect.collidepoint(mouse):
                    if len(utl.storyText) > 0:
                        if utl.Sound.upper() == "ENABLE":
                            sounds.playSound("success")
                        in_main_window = False
                        utl.storyLine = 0
                    else:
                        print("button disabled!")
                        #button disabled
                        #r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": utl.session_id, "message": "no story yet!"})
                        main.chatWindow.send_chatbot("no story yet!")

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
