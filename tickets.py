"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# 1. Create a list of 20 seats (numbered 1-20)
seats_available = [f"seat {i}" for i in range(1, 21)]

# 6. Repeat until user quits or seats are empty
while True:
    print("\nAvailable seats:")
    print(seats_available)

    # 3. Ask user for a seat number (0 to quit)
    choice = input("\nWhich seat do you want? (1–20, or 0 to quit): ")

    # Validate numeric input
    if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    choice = int(choice)

    if choice == 0:
        print("Goodbye!")
        break

    # 5. Handle invalid seat numbers
    if choice < 1 or choice > 20:
        print("That seat does not exist.")
        continue

    seat_name = f"seat {choice}"

    # 5. Handle seat already taken
    if seat_name not in seats_available:
        print("Sorry, that seat is already taken.")
        continue

    # 4. Remove the selected seat from the list
    seats_available.remove(seat_name)
    print(f"Your seat {choice} is confirmed!")

    # Stop if no seats left
    if not seats_available:
        print("\nAll seats are sold out!")
        break
