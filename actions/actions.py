# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
#from rasa_sdk.forms import FormAction
from pprint import pprint
import requests
import csv


class ValidateFarmForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_farm_form"
    
    def validate_farm(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text,Any]:

        flag = 0
        l = []
        csv_file = csv.reader(open("Farm.csv", "r"), delimiter=",")
        for row in csv_file:
            l.append(row[0])
        
        if slot_value.lower() not in l or slot_value is None:
            dispatcher.utter_message("Please select a valid farm. The farms available are:")
            for row in l:
                dispatcher.utter_message(row)
            return {"farm": None}
        else:
            return {"farm":slot_value}  



class ValidateMessageForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_message_form"
    
    def validate_farm(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text,Any]:

        if slot_value.lower() not in ['rams','greenery','nature','middle','animal']:
            dispatcher.utter_message(text=f"Unknown Farm. Please enter a valid farm name:")
            return {"farm": None}
        return {"farm":slot_value}



class ActionTempt(Action):
#
    def name(self) -> Text:
        return "action_tempt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

 
        API_key = "f68ad9b8d34b6523bd5dd00feca59e4a"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        farmname = tracker.get_slot('farm')
        
        csv_file = csv.reader(open("Farm.csv", "r"), delimiter=",")

        if farmname is None:
            dispatcher.utter_message('What is name of the farm?')
        else:
            for row in csv_file:
                if row[0] == farmname.lower():
                    latitude = str(row[1])
                    longitude = str(row[2])
            Final_url = base_url + "appid=" + API_key + "&lat=" + latitude + "&lon=" + longitude + "&units=metric"
            weather_data = requests.get(Final_url).json()    
            temp = weather_data['main']['temp']
            temp = str(temp)
            dispatcher.utter_message('The weather in ' + farmname + ' farm is ' + temp + " degree celsius") 
            dispatcher.utter_message('What else would you like to know about ' + farmname + ' farm?')

        return []

class ActionHumidity(Action):
#
    def name(self) -> Text:
        return "action_humidity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        API_key = "f68ad9b8d34b6523bd5dd00feca59e4a"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        farmname = tracker.get_slot('farm')
        
        csv_file = csv.reader(open("Farm.csv", "r"), delimiter=",")
    
        
        
        if farmname is None:
            dispatcher.utter_message('Please enter the name of the farm:')
        else:
            for row in csv_file:
                if row[0] == farmname.lower():
                    latitude = str(row[1])
                    longitude = str(row[2])
            Final_url = base_url + "appid=" + API_key + "&lat=" + latitude + "&lon=" + longitude +  "&units=metric"
            weather_data = requests.get(Final_url).json()    
            temp = weather_data['main']['humidity']
            temp = str(temp)
            dispatcher.utter_message('The humidity in ' + farmname + ' farm is ' + temp) 
            dispatcher.utter_message('What else would you like to know about ' + farmname + ' farm?')

        return []

class ActionWindspeed(Action):
#
    def name(self) -> Text:
        return "action_windspeed"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        API_key = "f68ad9b8d34b6523bd5dd00feca59e4a"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        

        farmname = tracker.get_slot('farm')

        csv_file = csv.reader(open("Farm.csv", "r"), delimiter=",")
        

        if farmname is None:
            dispatcher.utter_message('Please enter the name of the farm:')
        else:
            for row in csv_file:
                if row[0] == farmname.lower():
                    latitude = str(row[1])
                    longitude = str(row[2])
            Final_url = base_url + "appid=" + API_key + "&lat=" + latitude + "&lon=" + longitude +  "&units=metric"
            weather_data = requests.get(Final_url).json()    
            temp = weather_data['wind']['speed']
            temp = str(temp)
            dispatcher.utter_message('The speed of wind is ' + temp + ' km/hr') 
            dispatcher.utter_message('Would you like to know anything else about ' + farmname + ' farm?')

        return []


class ActionMessageRead(Action):
    def name(self) -> Text:
        return "action_message_read"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            csv_file = csv.reader(open("Message.csv", "r"), delimiter=",")
            dispatcher.utter_message('Checking...') 

            flag = 0
            
            farmname = tracker.get_slot('farm_message')
            if farmname is None:

                
                for row in csv_file:
                    #print(row[0])
                    if row[4] == '0':
                        dispatcher.utter_message('From ' + row[2] + ' at ' + row[0] + ': ' + row[1] + ' on ' + row[3] ) 

            else:
                for row in csv_file:
                    #print(row[1])
                    if row[4] == '0' and row[0] == farmname.lower():
                        flag = 1
                        dispatcher.utter_message('From ' + row[2] + ' at ' + row[0] + ': ' + row[1] + ' on ' + row[3] ) 
                if flag == 0:
                    dispatcher.utter_message('No messages.')
                
            
            return [SlotSet("farm_message", None)]

class ActionMessageReadFarm(Action):
    def name(self) -> Text:
        return "action_message_read_farm"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            csv_file = csv.reader(open("Message.csv", "r"), delimiter=",")
            flag = 0
            farmname = tracker.get_slot('farm')
            if farmname is None:
                for row in csv_file:
                    #print(row[0])
                    if row[4] == '0':
                        dispatcher.utter_message('From ' + row[2] + ' at ' + row[0] + ': ' + row[1] + ' on ' + row[3] ) 

            else:
                for row in csv_file:
                    #print(row[1])
                    if row[4] == '0' and row[0] == farmname.lower():
                        flag = 1
                        dispatcher.utter_message('From ' + row[2] + ' at ' + row[0] + ': ' + row[1] + ' on ' + row[3] ) 
                if flag == 0:
                    dispatcher.utter_message('No messages.')
                
            
            return []


class ActionMessageCount(Action):
    def name(self) -> Text:
        return "action_message_count"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            csv_file = csv.reader(open("Message.csv", "r"), delimiter=",")
            dispatcher.utter_message('Checking...') 

            count = 0
            
            farmname = tracker.get_slot('farm_message')
            if farmname is None:
                for row in csv_file:
                    #print(row[0])
                    if row[4] == '0':
                        count+=1

            else:
                for row in csv_file:
                    #print(row[1])
                    if row[4] == '0' and row[0] == farmname.lower():
                        count+=1

            if count == 0:
                dispatcher.utter_message('You have no unread messages')
            else:
                dispatcher.utter_message('You have ' + str(count) + ' messages')                
            
            return []


class ActionMessageCountFarm(Action):
    def name(self) -> Text:
        return "action_message_count_farm"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            csv_file = csv.reader(open("Message.csv", "r"), delimiter=",")
            dispatcher.utter_message('Checking...') 

            count = 0
            
            farmname = tracker.get_slot('farm')
            if farmname is None:
                for row in csv_file:
                    #print(row[0])
                    if row[4] == '0':
                        count+=1

            else:
                for row in csv_file:
                    #print(row[1])
                    if row[4] == '0' and row[0] == farmname.lower():
                        count+=1

            if count == 0:
                dispatcher.utter_message('You have no unread messages')
            elif count == 1:
                dispatcher.utter_message('You have 1 unread message.')
            else:
                dispatcher.utter_message('You have ' + str(count) + ' messages')                
            
            return []

class ActionExitFarm(Action):
    def name(self) -> Text:
        return "action_exit_farm"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
     
            
            return [SlotSet("farm", None)]


class ActionGateChange(Action):
#
    def name(self) -> Text:
        return "action_gate_change"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

 
        act = tracker.get_slot('act')
        if act == 'close':
            act = '1'
        else:
            act = '0'
        farmname = tracker.get_slot('farm')
        
        csv_file = csv.reader(open("Farm.csv", "r"), delimiter=",")
        if farmname:

            for row in csv_file:
                if row[0] == farmname.lower() and act == row[3]:
                    if act == '1':
                        dispatcher.utter_message(text="Gates are already closed.")
                    else:
                        dispatcher.utter_message(text="Gates are already opened.")
                elif row[0] == farmname.lower() and act != row[3]:
                    if act == '1':
                        dispatcher.utter_message(text="Closed gates")
                    else:
                        dispatcher.utter_message(text="Gates are now open.")
        else:
            for row in csv_file:
                if act == row[3]:
                    if act == '1':
                        dispatcher.utter_message("Gates in " + row[0] + " farm are already closed.")
                    else:
                        dispatcher.utter_message("Gates in " + row[0] + " farm are already opened.")
                elif act != row[3]:
                    if act == '1':
                        dispatcher.utter_message("Closed gates at " + row[0] + " farm.")
                    else:
                        dispatcher.utter_message("Gates are now open at " + row[0] + " farm.")


        return []


class ActionGate(Action):
#
    def name(self) -> Text:
        return "action_gate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        farmname = tracker.get_slot('farm')
        
        csv_file = csv.reader(open("Farm.csv", "r"), delimiter=",")
        if farmname:
            for row in csv_file:
                if row[0] == farmname.lower():
                    if row[3] == '1':
                        dispatcher.utter_message("Gates in " + row[0] + " farm are closed.")
                    else:
                        dispatcher.utter_message("Gates in " + row[0] + " farm are open.")
        else:
            for row in csv_file:
                    if row[3] == '1':
                        dispatcher.utter_message("Gates in " + row[0] + " farm are closed.")
                    else:
                        dispatcher.utter_message("Gates in " + row[0] + " farm are open.")
           

        return []

class ActionCrop(Action):
#
    def name(self) -> Text:
        return "action_crop_growth"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        farmname = tracker.get_slot('farm')
        
        csv_file = csv.reader(open("Farm.csv", "r"), delimiter=",")
        if farmname:
            for row in csv_file:
                if row[0] == farmname.lower():
                        dispatcher.utter_message("Crop growth in " + row[0] + " farm is at stage " +  row[4])

        else:
            for row in csv_file:
                dispatcher.utter_message("Crop growth in " + row[0] + " farm is at stage " +  row[4])
           

        return []

class ActionCrop(Action):
#
    def name(self) -> Text:
        return "action_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message('I can only help with managing your farms.')
        dispatcher.utter_message('Here is a list of your farms:')
        csv_file = csv.reader(open("Farm.csv", "r"), delimiter=",")
        for row in csv_file:
            dispatcher.utter_message(row[0])

        return []




            
            
            





