# app.py - Main script

from api_client import get_events
from display import show_events
from interaction import prompt_join_event
from utils import handle_error

def main():
    try:
        events = get_events()
        if not events:
            print('No upcoming events found.')
            return
        show_events(events)
        while prompt_join_event(events):
            pass
    except Exception as e:
        handle_error(e)

if __name__ == '__main__':
    main()
