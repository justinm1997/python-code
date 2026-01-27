"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f).
-----------------------------------------------------------------------
"""


# variables

Income = float(input("How much is your monthly income?     "))
Groceries = float(input("Amount spent on groceries?    "))
Monthly_memberships = float(input("Amount spent on monthly memberships?   "))
Pets = float(input("Amount spent on pets?    "))
video_games = float(input("Amount spent on video games?    "))
Monthly_bills = float(input("Amount spent on monthly bills?   ")) 



# Calculations

spent = Groceries + Monthly_memberships + Monthly_bills + video_games + Pets

remaining = Groceries - Monthly_memberships - Monthly_bills - video_games - Pets


# Output

print(f"You recieve {Income: ,.2f}")
print(f"You spend{spent: ,.2f} a month.")
print(f"You have {remaining: ,.2f} left")




