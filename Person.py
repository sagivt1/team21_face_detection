import database


class Person:

    def __init__(self):
        self.first_name = input("First Name:")
        self.last_name = input("Last Name:")
        self.i_d = input("enter your ID (9 digits):")
        while len(self.i_d) != 9:
            self.i_d = input("invalid number! please enter your id:")
        self.user_name = input("Please enter user name:")
        self.password = input("enter a password:")
        self.data = database.DataBase(self.first_name, self.last_name, self.i_d, self.user_name, self.password)
