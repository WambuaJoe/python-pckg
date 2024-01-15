#!/usr/bin/python3
import datetime
import uuid
import json


class EventManager:
    """the Event Manager class"""
    def __init__(self):
        """initialize class"""
        self.events ={}

    def create_event(self, event_name, event_date, *args, **kwargs):
        """create an event"""
        event_id = str(uuid.uuid4())
        event_datetime = datetime.datetime.strptime(event_date, '%d-%m-%Y, %H:%M %Z')
        event_details = {
            "name": event_name,
            "date": event_datetime.strftime('%d-%m-%Y, %H:%M %Z'),
            "notes": args,
            **kwargs
        }
        self.events[event_id] = event_details
        return event_id

    def update_event(self, event_id, **kwargs):
        """update event"""
        if event_id in self.events:
            event_details = self.events[event_id]
            event_details.update(kwargs)

    def list_event(self):
        """list events"""
        for event_id, event_details in self.events.items():
            print(f"Event ID: {event_id}")
            print(f"Event name: {event_details['name']}")
            print(f"Date of event: {event_details['date']}")
            if event_details['notes']:
                print(f"Notes: ")
                for note in event_details['notes']:
                    print(f" - {note}")
            print("AOB:")
            for key, value in event_details.items():
                if key not in ['name', 'date', 'notes']:
                    print(f"- {key}: {value}")
            print()

    def delete_event(self, event_id):
        """delete an event"""
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False
