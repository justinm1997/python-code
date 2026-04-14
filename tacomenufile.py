"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""


def get_menu_options():
    """Builds menu categories and items, saves to menu.txt."""
    menu = {}
    while True:
        print("Type 'Q' when done")
        category = input("Enter menu category (TACOS, PROTEIN, TOPPINGS): ").upper()
        if category == "Q":
            break
        items = input("Enter items separated by commas: ")
        menu[category] = items
    return menu


def save_to_file(menu):
    """Saves menu categories and items to menu.txt."""
    with open(MENU_FILE, "a") as file:
        for category, items in menu.items():
            file.write(f"{category}:{items}\n")


def menu_builder_main():
    my_menu = get_menu_options()
    save_to_file(my_menu)


def read_menu():
    """Reads menu.txt and returns dictionary."""
    menus = {}
    try:
        with open(MENU_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    category = parts[0].strip()
                    items = parts[1].strip()
                    menus[category] = items
        return menus
    except Exception as e:
        print(e)


def split_into_variables(menu_items):
    tacos = menu_items.get("TACOS")
    protein = menu_items.get("PROTEIN")
    tortillas = menu_items.get("TORTILLAS")
    toppings = menu_items.get("TOPPINGS")
    return tacos, protein, tortillas, toppings


def print_menu(tacos, protein, tortillas, toppings):
    print("\n--- TACO SHOP MENU ---\n")

    if tacos:
        print("Tacos:")
        for item in tacos.split(","):
            print(f"\t{item.strip()}")
    else:
        print("No taco items found.")

    if protein:
        print("\nProtein:")
        for item in protein.split(","):
            print(f"\t{item.strip()}")

    if tortillas:
        print("\nTortillas:")
        for item in tortillas.split(","):
            print(f"\t{item.strip()}")

    if toppings:
        print("\nToppings:")
        for item in toppings.split(","):
            print(f"\t{item.strip()}")


def menu_display_main():
    menu_items = read_menu()
    tacos, protein, tortillas, toppings = split_into_variables(menu_items)
    print_menu(tacos, protein, tortillas, toppings)


def audit_receipt(filename):
    """Reads receipt lines: qty,item,price and prints totals."""
    grand_total = 0.0
    try:
        with open(filename, "r") as f:
            for line in f:
                qty, name, price = line.strip().split(",")
                qty = int(qty)
                price = float(price)
                line_total = qty * price
                grand_total += line_total
                print(f"{qty}x {name} @ ${price:.2f} = ${line_total:.2f}")
    except FileNotFoundError:
        print("Error: Receipt file not found.")
    return grand_total


def audit_main():
    total = audit_receipt("taco_receipt.txt")
    print("-" * 30)
    print(f"GRAND TOTAL: ${total:.2f}")


audit_main()
