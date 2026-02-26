"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

import random

RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Without a doubt",
    "Most likely",
    "Don't count on it",
    "Signs point to yes",
)

print("Welcome to the Digital Oracle")
print("Ask any yes/no question or type 'quit' to exit.\n")

while True:
    question = input("What is your question?").strip().lower()

    if "quit" in question:
        print("Goodbye!")
        break

    answer = random.choice(RESPONSES)
    print(answer)


# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop
