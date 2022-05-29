# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from weather import Weather

class ActionFootballProducts(Action):
    def name(self) -> Text:
        return "action_football_products"


 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"Đây là danh sách {user_choice} mà cửa hàng đang bán:")

 
        if user_choice == "áo thể thao":
            dispatcher.utter_message(text="Bấm vào đây: [Link áo thể thao]")
        elif user_choice == "quần thể thao":
            dispatcher.utter_message(text="Bấm vào đây: [Link quần thể thao]")
        elif user_choice == "giày thể thao":
            dispatcher.utter_message(text="Bấm vào đây: [Link giày thể thao]")
        # else:
        #     dispatcher.utter_message(text="Vui lòng nhập đúng tên danh sách:")
        #
        return []


class ActionWeather(Action):
    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.latest_message['text']
        temp = int(Weather(city)['temp']-273)

        dispatcher.utter_template("utter_show_temp",tracker,temp=temp)

        return []
    
