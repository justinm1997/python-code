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

    return menu


def save_to_file(menu):

    # 4. Append ('a' mode) the new entry to our text file so it grows over time
    with open("menu.txt", "a") as file:
        all_items = menu.items()
        print(all_items)
        for item in all_items:
            item = item.split(",")
        # print(item) to check


def main():
    my_menu = get_menu_options()
    save_to_file(my_menu)


main()
