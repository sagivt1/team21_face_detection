from Person import Person
from database import DataBase
import RegularUser
import Tester


def Switcher(x, user):
    if x == 1:
        RegularUser.RegularUser.Register(user)
    elif x == 2:
        x.code = input("enter tester code:")
        Tester.Tester.Register(user, user.code)
    elif x == 3:
        x.code = input("enter manager code:")
        Manager.Register(user, user.code)
    return user


class Manager(Person):
    def __init__(self):
        Person.__init__(self)
        self.code = None

    def GivePermission(self, x=None):
        # input- self
        x = Person.register(x)
        choice = input("please select the user you'd want to give access:\n1.Regular User\n2.Tester\n Manager ")
        while choice != 1 or choice != 2 or choice != 3:
            print("invalid input!")
            choice = input("please select the user you'd want to give access:\n1.Regular User\n2.Tester\n Manager ")
        return Switcher(choice, x)

    def DeleteRegUser(self, reg):
        DataBase.delete_database(reg.data, reg.user_name)

    def DeleteTester(self, test):
        DataBase.delete_database(test.data, test.user_name)

    def DeleteManager(self, manager):
        DataBase.delete_database(manager.data, manager.user_name)
