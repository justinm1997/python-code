"""

creating the coffee class


"""


class Coffee:
    def __init__(self, coffee_type, size, milk, flavor, pumps):
        self.__coffee_type = coffee_type  # Double underscore makes it private (hides)
        self.__size = size
        self.__milk = milk
        self.__flavor = flavor
        self.__pumps = pumps
