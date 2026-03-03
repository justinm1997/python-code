"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

# what i typed to AI
# NATO_ALPHABET = { "A": "Alpha", "B": "Bravo", "C": "Charlie",  # ...COMPLETE A-Z } can you finish the rest of the alphabet


NATO_ALPHABET = {  # ...COMPLETE A-Z
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
}

word = input("Enter letter for word: ").upper()


try:
    letter = NATO_ALPHABET[word]
    print(f"System output: {letter}")
except KeyError:
    print(f"!! DATA INTEGRITY WARNING: '{word}' is not in our system.")


# TODO: Loop through each character
# TODO: try to print the NATO code, except if character is missing
