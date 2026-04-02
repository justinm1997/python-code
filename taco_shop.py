"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Taco shop
Developer: Justin Moravec
"""

# GLOBAL CONSTANTS (Pantry Rules)
MENU_FILE = "taco_menu"


def get_customer_info():
    """Asks for name and office location."""
    # TODO: Ask for name and order number
    return "Justin Moravec", "Order Number 1"


def take_order():
    """Collects taco category, tortilla, protein, and extras. Returns data."""
    # TODO: Capture tortilla (Flour/Corn) protein (Beef/Chicken/steak), and category (Taco/Buritto/Nachos)
    pass


def calculate_total(order_data):
    """Calculates price based on item type and extras."""
    # TODO: Load prices from taco_menu.txt

    return 7.50


def save_data_and_label(customer, total):
    """Appends to order_history.txt and prints the human-readable label."""
    # TODO: Write raw data for computer and formatted label for kitchen staff
    pass


def main():
    # 1. Identity Phase
    name, location = get_customer_info()
    print(f"Customer: {name} | Location: {location}")

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order)

    # 4. Handoff Phase
    save_data_and_label(name, final_price)


main()
