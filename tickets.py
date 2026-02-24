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

<<<<<<< HEAD
=======

>>>>>>> a856df4245ee8ce26c1e4ee34986a595ad17407a
seats = list(range(1, 21))


while True:
    print("\nAvailable seats:", seats)

    # Input validation

    choice = input("\nPick a seat number (0 to exit): ")

    if not choice.isdigit():
        print("\nPlease enter a valid number (1-20)")
        continue

    choice = int(choice)

    # Exit switch

    if choice == 0:
        print("\nGoodbye!")
        break

    # Seat check

    if choice in seats:
        seats.remove(choice)
        print(f"\nSeat {choice} sold!")
    else:
        print("\nSorry, that seat is not available")

    # Sold out

    if len(seats) == 0:
        print("\nAll seats are sold out! Goodbye!")
        break
    
