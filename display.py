# display.py - Functions to show information to the user

from utils import format_date

def show_events(events):
    print("\nUpcoming Events:\n")
    for idx, event in enumerate(events, 1):
        print(f"{idx}. {event['name']} on {format_date(event['date'])} (ID: {event['id']})")

