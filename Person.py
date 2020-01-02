
import database


class Person:

    def __init__(self, f_name, l_name, ID, user, passWord):

        self.first_name = f_name
        self.last_name = l_name
        self.id = ID
        self.user_name = user
        self.password = passWord

    def Register(self):
        self.first_name = input("First Name:")
        self.last_name=input("Last Name:")
        self.id = input("enter your ID (9 digits):")
        while len(self.id) != 9:
            self.id = input("invalid number! please enter your id:")
        self.user_name = input("Please enter user name:")
        self.password = input("enter a password:")
        database.DataBase.__init__(self,self.first_name,self.last_name,self.id,self.user_name ,self.password)

    def Login(self):
        self.user_name = input("Please enter user name:")
        self.password = input("enter a password:")
        while not database.DataBase.connect(self.user_name, self.password):
            print("WRONG USERNAME OR PASSWORD! PLEASE TRY AGAIN")
            self.user_name = input("Please enter user name:")
            self.password = input("enter a password:")

