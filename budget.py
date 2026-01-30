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

income = float(input("How much is your monthly income?     "))
groceries = float(input("Amount spent on groceries?    "))
monthly_memberships = float(input("Amount spent on monthly memberships?   "))
pets = float(input("Amount spent on pets?    "))
video_games = float(input("Amount spent on video games?    "))
monthly_bills = float(input("Amount spent on monthly bills?   "))

# Calculations

spent = groceries + monthly_memberships + monthly_bills + video_games + pets

remaining = income - groceries - monthly_memberships - monthly_bills - video_games - pets

percent = remaining/income 



# Output

print(f"You recieve ${income: ,.2f} a month")
print(f"You spend ${spent: ,.2f} a month.")
print(f"You have ${remaining: ,.2f} left")
print(f"You spent {percent: ,.2f}% On Monthly cost")

