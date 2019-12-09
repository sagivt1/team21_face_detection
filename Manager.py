import Person


class Manager(Person):
    def __init__(self, f_name, l_name, ID, user, passWord):
        self.f_name = f_name
        self.passWord = passWord
        self.user = user
        self.ID = ID
        self.l_name = l_name
