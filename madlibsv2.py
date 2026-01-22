"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS - Madlibs
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Assignment Name, Date, File Name).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""


# Justin loves to play video games

print("\n\n\nJustin loves to play video games especially Call Of Duty untill Mid-Night.")
print("Justin is 28 years old and also enjoys to Work out.")
print("Justin is usually in a great mood every day.")

#   Variables 

person_name =  input("Person's name:   ")
videogames = input("Videogame's name    ")
time_of_day = input("Time of day(Morning, Afternoon, Mid-Night)    ")
person_age = input("Your Age   ")
activity = input("What do you like to do in your spare time    ")
mood = input("Your mood    ")


#   Outputs

print(f"\n\n\n{person_name} loves to play video games especially {videogames} untill {time_of_day}.")
print(f"{person_name} is {person_age} years old and also enjoys to {activity}.")
print(f"{person_name} is usually in a {mood} mood every day. ")






