"""
ASSIGNMENT 11A - THE OFFICE HERO DASHBOARD
This program processes office supply expenses and returns both
a calculated total (with tax) and a status message describing
the type of purchase.
"""

# ---------------------------------------------------------
# GLOBAL CONSTANTS
# ---------------------------------------------------------
OFFICE_NAME = "The Office Hero"
TAX_RATE = 0.05


def process_expenses(price, quantity):

    subtotal = price * quantity
    tax_amount = subtotal * TAX_RATE
    final_total = subtotal + tax_amount

    # Create a status message
    status = "Bulk Order" if quantity >= 10 else "Standard Order"

    return final_total, status


def main():
    print(f"Welcome to {OFFICE_NAME} Expense Processor!\n")

    try:
        item_price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price. Defaulting to 1.00")
        item_price = 1.00

    try:
        item_qty = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity. Defaulting to 1")
        item_qty = 1

    total_cost, order_status = process_expenses(price=item_price, quantity=item_qty)

    print("\n Expense Summary")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Order Type: {order_status}")


main()
