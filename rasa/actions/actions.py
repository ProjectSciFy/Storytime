# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
import pygame
import json

import sys
sys.path.append("..") 
from generate import generateSampleStory
import utility as utl
#from helpers import updateScheme, updateFont, updateSound

class ActionSayKeywords(Action):

    def name(self) -> Text:
        return "action_say_keywords"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        keyword1 = tracker.get_slot("keyword_1")
        keyword2 = tracker.get_slot("keyword_2")
        keyword3 = tracker.get_slot("keyword_3")
        keyword4 = tracker.get_slot("keyword_4")

        keywords = [keyword1, keyword2, keyword3, keyword4]

        string_keywords = " ".join(keywords)
        [image_paths, sentences, storyNumber] = generateSampleStory(string_keywords, "sample author")

        utl.storyText = sentences
        numOfEntries = len(sentences)
        utl.storyImages = [pygame.transform.scale(pygame.image.load(f"./images/story_{storyNumber}/sentence_{i}.png"), (508, 508)) for i in range(numOfEntries)]
        
        with open('rasa_pass.json','r+') as f:
            data = json.load(f)
            data['keywords'] = keywords
            data['story'] = sentences
            data['image_paths'] =image_paths
            data['story_num'] = storyNumber
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        #message = returnToRasa(keywords)
        #dispatcher.utter_message(message)

        dispatcher.utter_message(text=f"Thanks! Your story in on the story page with the keywords {keyword1} {keyword2} {keyword3} {keyword4}.")

        return []
    

class ActionResetForm(Action):
    def name(self) -> Text:
        return "action_reset_form"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [AllSlotsReset()]
    
class ActionUpdateColor(Action):
    def name(self) -> Text:
        return "action_update_color"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        scheme = tracker.get_slot("scheme")

        with open('rasa_pass.json','r+') as f:
            data = json.load(f)
            data['scheme'] = scheme
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
       
        dispatcher.utter_message(text=f"Updating scheme to {scheme}.")

        return []
    
class ActionUpdateFont(Action):
    def name(self) -> Text:
        return "action_update_font"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        from helpers import updateFont
        font = tracker.get_slot("font")
        with open('rasa_pass.json','r+') as f:
            data = json.load(f)
            data['font'] = font
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
        dispatcher.utter_message(text=f"Updating font to {font}.")
        
        return []
    
class ActionUpdateSound(Action):
    def name(self) -> Text:
        return "action_update_sound"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        from helpers import updateSound
        sound = tracker.get_slot("sound")
        with open('rasa_pass.json','r+') as f:
            data = json.load(f)
            data['sound'] = sound
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
        dispatcher.utter_message(text=f"Updating sound to {sound}.")
        
        return []