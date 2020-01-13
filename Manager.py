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
        choice = input("please select the user you'd want to give access:\n1.Regular User\n2.Tester\n 3 Manager ")
        while choice != 1 or choice != 2 or choice != 3:
            print("invalid input!")
            choice = input("please select the user you'd want to give access:\n1.Regular User\n2.Tester\n 3.Manager ")
        while

    def DeleteRegUser(self, reg):
        reg.data.delete_database(reg.user_name)

    def DeleteTester(self, test):
        test.data.delete_database(test.user_name)

    def DeleteManager(self, manager):
        manager.data.delete_database(manager.user_name)

    def edit_user_details(self, user_name):  # todo: get user's user name from main
        choice = input(
            "please select the detail you'd like to edit:\n 1.first name\n 2.last name: \n 3.user name \n 4.ID \n 5.password\n 9.exit\n")
        while choice is not 9:
            choice = input(
                "please select the detail you'd like to edit:\n 1.first name\n 2.last name: \n 3.user name \n 4.ID \n 5.password\n 9.exit\n")
            while choice != 1 or choice != 2 or choice != 3 or choice != 4 or choice != 5 or choice != 9:
                print("invalid input!")
                choice = input(
                    "please select the detail you'd like to edit:\n 1.first name\n 2.last name: \n 3.user name \n 4.ID \n 5.password\n 9.exit\n")
            if choice == 1:

            elif choice == 2:

            elif choice == 3:

            elif choice == 4:

            elif choice == 5:

            else choice == 9:
                return

    def access_to_all_users(self):

    def view_all_the_users(self):

    def users_amount_report(self):

    def add_user(self):
    def active_users_report(self):
    def view-user_contacts(self):
    def report_fail_to