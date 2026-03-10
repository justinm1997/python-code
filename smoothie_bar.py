"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# TODO: Define get_price(size)

# TODO: Define blend(size, base, fruit, scoops)

# TODO: Define main() to collect input and call your logic

def get_price(size):
    if size == "small":
        return 1.00
    elif size == "medium":
        return 2.00
    else:
        return 3.00


def get_blend(size, base, fruit, scoops):
    print("Smoothie order")
    print(f"Size: {size}")
    print(f"base: {base}")
    print(f"fruit:  {fruit}  ({scoops} scoops)")




def main():
    print("Welcome to the smoothie bar!" )

    choice_size = input("size (small/medium/large): ").title().strip()
    choice_base = input("Select base: ")
    choice_fruit = input("select fruit: ")

    try:
        packets = int(input("how many scoops of fruit: "))
    except ValueError:
        print("Invalid entry. defaulting to 1. ")
        packets = 1
    
    cost = get_price(choice_size)

    get_blend(choice_size, choice_base, choice_fruit, packets)
   
    print(f"Total Bill ${cost:.2f}")




main()

