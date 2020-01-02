from Person import Person
import database


class Tester(Person):
    def __init__(self, f_name, l_name, ID, user, passWord):
        Person.__init__(self, f_name, l_name, ID, user, passWord)

    def Register(self, code):
        self.code = input("enter tester code:")
        while self.code != 1111:
            self.code = input("wrong code! please enter tester code:")

    def Login(self): self.Login(Person)
