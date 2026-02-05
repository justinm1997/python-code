"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# task 1

the_nagging_kid = True

while the_nagging_kid:
    print("Are we there yet?  ")

    # We must change the state to stop the loop

    answer = input("Are we finally here? (y/n):   ")
    if answer == "y" or answer == "Y":
        the_nagging_kid = False


# task 2
