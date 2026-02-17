"""
Docstring for lists
"""

months = ["January", "feburary"]


days_in_months = [
    31,
    28,
]


for i in range(0, 12):
    print(f"{months[i]} has {days_in_months[i]} days")

    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    steps = []


    for day in days_of_week:
    daily_steps = int(input(f"How many steps did you take on {day}:  "))
    steps.append(daily_steps)


    for i in range(0,7):
        print(f"{days_of_week[i]} you took {steps[i]}:,.2f")


    print(f"You took a total of {sum(steps)}")


