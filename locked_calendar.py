"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

for month in MONTHS:
    print(f"{month}")

    print("\nAttempting illegal modification...")

try:
    # Tuples are physically locked. This triggers a TypeError.
    MONTHS[0] = "NewMonth"  # this will cause a type error

except TypeError:
    print("Error: System settings are locked and immutable! ")


# This assignment fails because tuples are immutable.
# That means once a tuple is created, its elements cannot be changed,
# added, or removed. Attempting to assign a new value causes a TypeError.
