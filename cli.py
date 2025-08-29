# cli.py
from display import show_products
from recommendations import find_eco_friendly, suggest_alternatives
from logger import log_user_choice

def start_cli(products):
    print("Eco-Friendly Shopping Assistant")
    eco_products = find_eco_friendly(products)
    print("\nHighly Sustainable Products:")
    show_products(eco_products)
    choice = int(input("\nSelect a product number for alternatives or 0 to exit: "))
    if choice == 0:
        print("Goodbye!")
        return
    selected_product = eco_products[choice -1]
    print(f"\nAlternatives for {selected_product['name']}:")
    alternatives = suggest_alternatives(products, selected_product)
    show_products(alternatives)
    log_user_choice(selected_product)
    print("Your choice has been logged.")
