from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDiagnose(Action):
    def name(self):
        return "action_diagnose"

    def run(self, dispatcher, tracker, domain):
        symptom = tracker.get_slot("SYMPTOM")
        if symptom == "fever":
            dispatcher.utter_message(text="You might have a cold. Rest and hydrate!")
        else:
            dispatcher.utter_message(text="I’d suggest seeing a doctor.")
        return []
