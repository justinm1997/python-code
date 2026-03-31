"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

TOPPINGS = ("pepperoni", "sausage", "veggies", "mushrooms")


def make_pizza(customer, size, topping, is_delivery=False):

    print(f"\n--- OFFICIAL TICKET: {customer.upper()} ---")
    print(f"Pizza size: {size}")
    print(f"Topping: {topping}")
    print(f"Delivery {is_delivery}")


def main():
    user = input("Customer Name: ")
    print(f"Available Toppings: {TOPPINGS}")
    topping_choice = input("Select topping: ").title()

    try:
        size_choice = input("Choose size(Small/Medium/Large):  ").title()
    except ValueError:
        print("Invalid input. Defaulting to Medium")
        size = "Medium"

    make_pizza(
        customer=user,
        size=size_choice,
        topping=topping_choice,
    )


main()
