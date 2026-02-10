"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# 1. Validate First Name (Cannot be blank)
first_name = input("Enter First Name: ")
while first_name == "":
    print("❌ Error: Name cannot be blank.")
    first_name = input("Please enter First Name: ")

# 1. Validate last Name (Cannot be blank)
last_name = input("Enter Last Name: ")
while last_name == "":
    print("❌ Error: Name cannot be blank.")
    last_name = input("Please enter Last Name: ")


# 2. Validate Chaperone Status (Must be Y or N)
chaperone = input("Parent volunteering to chaperone? (Y/N): ").upper()
while chaperone != "Y" and chaperone != "N":
    print("❌ Error: Please enter only Y or N.")
    chaperone = input("Parent volunteering to chaperone? (Y/N): ").upper()


print(f"\n✅ Registration Complete for {first_name}!")

# 3. Phone number ( cannot be blank )
phone_number = input("Enter your phone number ")
while phone_number == "":
    print("❌ Error: phone number cannot be blank.")
    phone_number = input("Please enter phone number: ")


# 4. Validate Ticket Count (Must be an Integer)
tickets = 0
while True:
    try:
        tickets = int(input("How many tickets? "))
        if tickets > 0:
            break  # Valid number! Escape the loop!
        print("❌ Error: Must be at least 1 ticket.")
    except ValueError:
        print("❌ Error: Please enter a NUMBER (e.g., 5, not 'five').")

print(f"✅ Ordered {tickets} tickets.")
