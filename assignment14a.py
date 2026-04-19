"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

class TacoOrder:
    def __init__(self, category, tortilla, protein, extras):
        # Private attributes protect the order details
        self.__category = category
        self.__tortilla = tortilla
        self.__protein = protein
        self.__extras = extras

    # Getters 
    def get_category(self):
        return self.__category

    def get_protein(self):
        return self.__protein

    # Setters
    def set_protein(self, protein):
        # Setters allow us to validate data before changing it
        if protein in ("Beef", "Chicken", "Steak"):
            self.__protein = protein

    # Summary Output
    def get_summary(self):
        return (f"Order Summary: {self.__category} with {self.__tortilla} tortilla, "
                f"{self.__protein} protein, and extras: "
                f"{', '.join(self.__extras) if self.__extras else 'None'}.")
        

# Using the objects
order1 = TacoOrder("Taco", "Corn", "Beef", ["Cheese", "Salsa"])
print(order1.get_summary())

