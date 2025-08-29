# interaction.py - Handle user input and interactions

from api_client import join_event

def prompt_join_event(events):
    try:
        choice = int(input('\nEnter event number to join or 0 to exit: '))
        if choice == 0:
            print('Exiting.')
            return False
        if 1 <= choice <= len(events):
            event_id = events[choice - 1]['id']
            success = join_event(event_id)
            if success:
                print('Successfully joined the event!')
            else:
                print('Failed to join the event.')
        else:
            print('Invalid choice.')
    except ValueError:
        print('Enter a valid number.')
    return True

