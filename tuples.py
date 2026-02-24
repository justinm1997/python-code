"""
demonstrate tuples and constants
"""

SCHOOL_NAME = "Mchenry County College"

SEMESTER = (
    "1. Spring",
    "2. Summer Intersession",
    "3. Summer",
    "4. Fall",
    "5. Winter Intersession",
)

try:
    # This will fail because tuples are immutable
    SEMESTER[0] = "Spring Break"

    for semester in SEMESTER:
        print(semester)

    semester = int(
        input("Please enter the number of the semester you want to register for: ")
    )

except TypeError:
    print("That is not allowed to be changed")

except Exception as e:
    print(e)
