from Person import Person


class Manager(Person):
    def __init__(self, f_name, l_name, ID, user, passWord, code):
        Person.__init__(self, f_name, l_name, ID, user, passWord)
        self.code = None

    def Register(self, code):
        self.code = input("enter manager code:")
        while self.code != 0000:
            self.code = input("wrong code! please enter manager code:")


    def Login(self): self.Login(Person)