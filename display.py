# display.py
def show_products(products):
    for i, p in enumerate(products, 1):
        print(f"{i}. {p['name']} (Score: {p['sustainability_score']}, {p['category']})")

