# utils.py - Utility functions

from datetime import datetime

def format_date(date_str):
    dt = datetime.fromisoformat(date_str)
    return dt.strftime('%b %d, %Y')

def handle_error(e):
    print(f"Error: {e}")
