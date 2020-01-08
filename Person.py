import database


class Person:

    def __init__(self,first_name,last_name,i_d,user_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.i_d = i_d
        self.user_name = user_name
        self.password = password
        self.data = database.DataBase(self.user_name)

