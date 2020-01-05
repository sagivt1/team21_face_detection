
import database


class Person:

    def __init__(self, f_name = None, l_name = None, ID = None, user = None, password = None):

        self.data = database.DataBase(self.first_name,self.last_name,self.id,self.user_name,self.password)
        self.first_name = f_name
        self.last_name = l_name
        self.id = ID
        self.user_name = user
        self.password = password

    def register(self):
        self.first_name = input("First Name:")
        self.last_name=input("Last Name:")
        self.id = input("enter your ID (9 digits):")
        while len(self.id) != 9:
            self.id = input("invalid number! please enter your id:")
        self.user_name = input("Please enter user name:")
        self.password = input("enter a password:")

    def login(self):
        self.user_name = input("Please enter user name:")
        self.password = input("enter a password:")
        while not database.DataBase.connect(self.user_name, self.password):
            print("WRONG USERNAME OR PASSWORD! PLEASE TRY AGAIN")
            self.user_name = input("Please enter user name:")
            self.password = input("enter a password:")

