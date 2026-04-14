"""

Demonstrate classes and objects based on the monty coffee project

"""


class Employee:
    # class names are capitalized
    def __init__(self, fname, lname, extension, emp_num):
        self.fname = fname
        self.lname = lname
        self.extension = extension
        self.emp_num = emp_num

    # setters
    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname

    def set_extension(self, extension):
        self.extension = extension

    def set_emp_num(self, emp_num):
        self.emp_num = emp_num

    # getters
    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_extension(self):
        return self.extension

    def get_emp_num(self):
        return self.emp_num

    # descriptions
    def description(self):
        print(
            f"{self.fname} {self.lname} \nextension: {self.extension} \nemployee number: {self.emp_num}"
        )

    """
    create an employee object
    """

    emp1 = Employee("Justin", "Moravec", "40404", 222)
    emp2 = Employee("Monty", "Pyduck", "23232", 982)

    print(emp1.get_fname(), emp1.get_lname())
    emp2.description()
