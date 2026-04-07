"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Taco Shop (V3.0)
Developer: Justin Moravec
"""

# GLOBAL CONSTANTS (Pantry Rules)
MENU_FILE = "menu.txt"
TORTILLA_OPTIONS = ("Corn", "Flour")
MEAT_OPTIONS = ("Chicken", "Beef", "Steak")
TOPPING_OPTIONS = ("Lettuce", "Tomato", "Cheese", "Onion", "Salsa")

def get_customer_info():
    """Asks for name and Table number."""
    name = input("Customer Name: ").title()
    location = input("Table Number: ")
    return name, location

def take_order():
    """Collects taco category, tortilla, protein, and extras. Returns data."""

    # Category selection
    print("Category Options: Taco / Burrito / Nachos")
    category = input("Choose category: ").title()

    # Tortilla selection
    print("Tortilla Options: Flour / Corn")
    tortilla = input("Choose tortilla: ").title()

    # Protein selection
    print("Protein Options: Beef / Chicken / Steak")
    protein = input("Choose protein: ").title()

    # Extras (comma separated)
    extras = input("Extras (comma separated, e.g., Cheese, Salsa, Onion): ")
    extras_list = [e.strip().title() for e in extras.split(",")] if extras else []

    return {
        "category": category,
        "tortilla": tortilla,
        "protein": protein,
        "extras": extras_list
    }

def calculate_total(order_data):
    """Calculates price based on category, protein, and extras."""

    # Base prices by category
    category_prices = {
        "Taco": 3.00,
        "Burrito": 8.00,
        "Nachos": 10.00
    }

    # Protein upcharges
    protein_upcharge = {
        "Beef": 1.00,
        "Chicken": 1.00,
        "Steak": 2.00
    }

    # Extras cost (each)
    extra_cost = 0.50

    # Determine base price
    base = category_prices.get(order_data["category"], 3.00)

    # Add protein cost
    protein_cost = protein_upcharge.get(order_data["protein"], 0)

    # Add extras cost
    extras_total = len(order_data["extras"]) * extra_cost

    return base + protein_cost + extras_total

def save_data_and_label(customer, location, total, order_data):
    """Appends to order_history.txt and prints the human-readable label."""
    print(f"--- KITCHEN TICKET ---")
    print(f"TABLE NUMBER: {location} | ATTN: {customer}")
    print(f"ITEM: {order_data['category']}")
    print(f"TORTILLA: {order_data['tortilla']}")
    print(f"PROTEIN: {order_data['protein']}")
    print(f"EXTRAS: {', '.join(order_data['extras']) if order_data['extras'] else 'None'}")
    print(f"TOTAL: ${total:.2f}")

def main():
    # 1. Identity Phase
    name, location = get_customer_info()

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order)

    # 4. Handoff Phase (Using KEYWORD ARGUMENTS)
    save_data_and_label(customer=name, location=location, total=final_price, order_data=current_order)

main()