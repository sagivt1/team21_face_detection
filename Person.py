import database


class Person:

    def __init__(self,first_name,last_name,i_d,user_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.i_d = i_d
        self.user_name = user_name
        self.password = password
        self.data = database.DataBase(self.user_name)


<<<<<<< HEAD
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
=======
>>>>>>> ed694b208f22e1830f25266a8aac78fe6bf01ce7
