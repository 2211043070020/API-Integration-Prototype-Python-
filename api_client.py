# api_client.py - Functions for MeetMux API calls

import requests
from config import API_KEY, BASE_URL

HEADERS = {
    'Authorization': f'Bearer {API_KEY}'
}

def get_events():
    url = f'{BASE_URL}/events'
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('events', [])

def join_event(event_id, user_id='demo-user'):
    url = f'{BASE_URL}/events/{event_id}/join'
    payload = {'userId': user_id}
    response = requests.post(url, json=payload, headers=HEADERS)
    response.raise_for_status()
    return response.ok
