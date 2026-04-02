"""

writing to files
date/time
create menu text file for coffee house

"""

import datetime


def get_menu_options():
    # get info for menu dictionary
    menu = {}
    while True:
        print("Type Q when done")
        category = input(
            "please give me the category for this part of the menu:  "
        ).upper()
        if category == "Q":
            break
        items = input("please enter items separated by commas: ")

        # add to dictionary
        menu[category] = items

    print(menu)

    return menu


def save_to_file(menu):
    pass
    # 3. Store it in a dictionary using the timestamp as the key
    # health_log = {timestamp_str: blood_sugar}

    # 4. Append ('a' mode) the new entry to our text file so it grows over time
    # with open("blood_sugar_log.txt", "a") as file:
    #    file.write(f"[{timestamp_str}] : {health_log[timestamp_str],}\n")


def main():
    my_menu = get_menu_options()
    save_to_file(my_menu)


main()
