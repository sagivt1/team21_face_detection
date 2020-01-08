import database


class Person:

    def __init__(self):

        self.data = None
        self.first_name = None
        self.last_name = None
        self.i_d = None
        self.user_name = None
        self.password = None

    def register(self):
        self.first_name = input("First Name:")
        self.last_name = input("Last Name:")
        self.i_d = input("enter your ID (9 digits):")
        while len(self.i_d) != 9:
            self.i_d = input("invalid number! please enter your id:")
        self.user_name = input("Please enter user name:")
        self.password = input("enter a password:")
        self.data = database.DataBase(self.first_name, self.last_name, self.i_d, self.user_name, self.password)
        return True

    def login(self):
        user_name = input("Please enter user name:")
        password = input("enter a password:")
        if not database.DataBase.connect(self.data, user_name, password):
            print("WRONG USERNAME OR PASSWORD! PLEASE TRY AGAIN")
            return False

        return True
