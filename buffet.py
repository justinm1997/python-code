"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

# Variables

age = int(input("How old are you (0-99)?    "))

#calculations 

final_price = 1 * age
under1_price = 0
standard_adult_price = 16.95
senior_discount_price = 12.95
over_age_price = 0


if age < 1:
    print("Kids under 1 eat free!($0.00)    ")
    print(f"You owe ${under1_price: ,.2f} ")

elif age <= 11:
    print("$1.00 per year of age (Example: 5 years = $5.00) ")
    print(f"You owe ${final_price: ,.2f} ")

elif age <= 64:
    print("$16.95 (Standard Adult) ")
    print(f"You owe ${standard_adult_price: ,.2f} ")

elif age <= 99:
    print("$12.95 (Senior Discount) ")
    print(f"You owe ${senior_discount_price: ,.2f} ")

else:
    print("Wow! You're alive!? ")
    print("You can eat free on the house :) ")
    print(f"You owe ${over_age_price: ,.2f} ")

