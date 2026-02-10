"""
input validation
"""

# Rent a car

first_name = ""
while len(first_name) == 0:
    first_name = input("What is your legal first name?  ")


first_name = ""
while len(first_name) == 0:
    first_name = input("What is your legal first name?  ")

age = ""
while age < 16 or len(age) == 0:
    age = input("What is your age?   ")
    if age < 0 or age > 70:
        print("I'm sorry, that is not a valid age")
    elif age > 24:
        pass
    else:
        print("I'm sorry, we cannot rent to you")


valid = input("Do you have a valid drivers license (Y/N)").upper
if valid == "Y":
    pass
else:
    print("I'm sorry, we cannot rent to you   ")
