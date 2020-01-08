from datetime import date

from Person import Person
import database


class Tester(Person):
    def __init__(self, f_name, l_name, ID, user, passWord):
        Person.__init__(self)
        self.code = None

    def Register(self, code):
        if code == '1111':
            Person.register(self)
            self.data.create_detection_table(self.user_name)
            self.data.create_contact_list_table(self.user_name)
            self.data.create_fail_list(self.user_name)

    def Login(self): Person.login(self)

    def ReportFail(self):
        print("enter the fail details: \n")
        fail_name = input("fail name:\n")
        fail_description = input("fail description:\n")
        status = input("fail status: \n")
        database.DataBase.add_fail(self.data, self.user_name, date.day, date.month, date.year, fail_name,
                                   fail_description, status)
