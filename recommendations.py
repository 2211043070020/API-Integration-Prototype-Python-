# recommendations.py
def find_eco_friendly(products, threshold=70):
    return [p for p in products if p['sustainability_score'] >= threshold]

def suggest_alternatives(products, selected_product):
    category = selected_product['category']
    alternatives = [p for p in products if p['category'] == category and p['id'] != selected_product['id']]
    return sorted(alternatives, key=lambda x: -x['sustainability_score'])
