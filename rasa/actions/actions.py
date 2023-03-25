# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


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

        dispatcher.utter_message(text=f"Thanks! Your story in on the story page with the keywords {keyword1} {keyword2} {keyword3} {keyword4}.")

        return []
