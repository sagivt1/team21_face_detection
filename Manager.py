from Person import Person


class Manager(Person):
    def __init__(self, f_name, l_name, ID, user, passWord):
        Person.__init__(self, f_name, l_name, ID, user, passWord)

