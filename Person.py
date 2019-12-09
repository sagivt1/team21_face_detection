import database


class Person:

    def __init__(self, f_name, l_name, ID, user, passWord):
        self.first_name = f_name
        self.last_name = l_name
        self._id = ID
        self._user_name = user
        self._password = passWord
        self.data = database.DataBase()

