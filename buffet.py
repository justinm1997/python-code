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

age = int(input("How old are you?(1-99)    "))


if age <= 1:
    print("Kids under 1 eat free!($0.00)    ")

if age <= 1-11:
    print("1.00 per year of age(Example: 5 years = $5.00)    ")

if age <= 12-64:
    print("$16.95 (Standard Adult)   ")

if age <= 65-99:
    print("$12.95 (Senior Discount)   ")




