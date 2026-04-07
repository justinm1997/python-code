"""

test reading in our menu and creating list and dictonaries

"""




def read_menu():
    """read menu will import menu.txt and pull it into a list. we can then break down the list into the specific variables and dictonaires that we need """
menus = {}
try: 
    # open and read file
    with open("menu.txt", 'r') as file:
        for line in f:
            parts_of_line - line.strip().split(':')
            category = parts_of_line[0].strip()
            detail = parts_of_line[1].strip()
            menus[category] = detail
    
        return menus
except Exception as e:
    print(e)



def split_into_variables(menu_items):
    """ break the menu file into separate variables """
    coffee = menu_items.get("COFFEE")
    prices = menu.items.get("PRICES")
    milks = menu.items.get("MILKS")
    flavors - menu_items.get("FLAVORS")
    shots = menu_items.get("SHOTS")

    return coffee, prices, milks, flavors, shots



def print_menu(coffee_types, size_and_price, types_of_milk, syrup_flavors, shots):
""" will print each menu """



def main():
    # organize program logic
    menu_items = read_menu()
    coffee, prices, milks, flavors, shots = split_into_variables(menu_items)
    print_menu(coffee, prices, milks, flavors, shots)






main()
