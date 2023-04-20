# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.types import DomainDict

import pygame
import json

import sys
sys.path.append("..") 
from generate import generateSampleStory
import utility as utl
#from helpers import updateScheme, updateFont, updateSound

class ValidateKeywordFillingForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_keyword_filling_form"

    def validate_keyword_1(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value == "no story yet!":
            dispatcher.utter_message(text="Sorry you need to enter keywords to generate a story first")
            return {"keyword_1": None}
        return {"keyword_1": slot_value}
    
    def validate_keyword_2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value == "no story yet!":
            dispatcher.utter_message(text="Sorry you need to enter more keywords, restarting keyword collection.")
            return {"keyword_2": None}
        return {"keyword_2": slot_value}
    
    def validate_keyword_3(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value == "no story yet!":
            dispatcher.utter_message(text="Sorry you need to enter more keywords, restarting keyword collection.")
            return {"keyword_3": None}
        return {"keyword_3": slot_value}

    def validate_keyword_4(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        if slot_value == "no story yet!":
            dispatcher.utter_message(text="Sorry you need to enter more keywords, restarting keyword collection.")
            return {"keyword_4": None}
        return {"keyword_4": slot_value}

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

        dispatcher.utter_message(text=f"Your story is currently being generated, this will take a minute.")

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
    
class ActionShowStoredTitles(Action):
    def name(self) -> Text:
        return "action_show_stored_titles"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        titles = ['The Dragon and the Bear','A Mining Adventure','Battle for the World','Story Title 57']
        title_string =  ", ".join(titles)
        dispatcher.utter_message(text=f"Your library contains the following titles: {title_string}")
        
        return []
    
class ActionLoadStory(Action):
    def name(self) -> Text:
        return "action_load_story"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        titles = ['The Dragon and the Bear','A Mining Adventure','Battle for the World','Story Title 57']
        title_string =  ", ".join(titles)

        title = tracker.get_slot("title")

        title_found = False
        dispatcher.utter_message(title)
        for lib_title in titles:
            if title.lower() in lib_title.lower():
                title = lib_title
                title_found = True
        if title_found:
            dispatcher.utter_message(text=f"Thanks! {title} in on the story page.")

        else:
            dispatcher.utter_message(text=f"Sorry! That title is not in the library. Your library contains the following titles: {title_string}")
        
        return []