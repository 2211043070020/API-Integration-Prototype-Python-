# logger.py
import json
import os

LOG_FILE = 'user_log.json'

def log_user_choice(product):
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            logs = json.load(f)
    logs.append(product)
    with open(LOG_FILE, 'w') as f:
        json.dump(logs, f, indent=2)
