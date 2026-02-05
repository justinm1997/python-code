"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# num 1
life_level = int(input("What level are you in life?(0-100)  "))

# num 2
age = int(input("How old are you? "))

# if/else/elif

if life_level >= 95:
    level = "You're a Master at life!"
elif life_level >= 80:
    level = "You're a Professional at life!"
elif life_level >= 70:
    level = "You're a close to success keep going!"
elif life_level >= 50:
    level = "Keep working, the success will come!"
elif life_level >= 30:
    level = "Everyone starts somewhere, keep on climbing!"
else:
    level = "You have to keep climbing to be a master!"


if age >= 80:
    age_description = "You're full of wisdom"
elif age >= 65:
    age_description = "You're a senior citizen"
elif age >= 30:
    age_description = "You're still a young adult"
elif age >= 18:
    age_description = "You're an adult now welcome to the club!"
elif age >= 13:
    age_description = "Welcome to your teens, don't blink it goes by fast!"
else:
    age_description = "Wow, you're so young like a baby!"


# Logical checks


# outputs

print(f"{level}")
print(f"{age_description}")
