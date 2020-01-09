from Person import Person


class Manager(Person):
    def __init__(self):
        Person.__init__(self)
        self.code = None

    def Register(self, code):

        self.code = input("enter manager code:")
        while self.code != 0000:
            self.code = input("wrong code! please enter manager code:")


    def Login(self): Person.login(self)