# data_loader.py
import json
from config import DATA_FILE

def load_products():
    with open(DATA_FILE, 'r') as file:
        products = json.load(file)
    return products

