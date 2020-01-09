from Person import Person
from database import DataBase


class Tester(Person):
    def __init__(self):
        Person.__init__(self)
        self.code = None

    def Register(self):

        code = input("Enter the tester code :")
        while code != '1111':
            code = input("invalid number! Enter the tester code :")
        Person.register(self)
        self.data.create_detection_table(self.user_name)
        self.data.create_contact_list_table(self.user_name)
        self.data.create_fail_list(self.user_name)

    def Login(self):
        Person.login(self)

    def report_of_problems(self): # todo: create a file with problems
        """
                 :return:
                 """
        pass


    def report_of_urgent_problems(self):  # todo: create a file with urgent problems
        """
         :return:
        """
        pass

    def daily_report(self):  # todo: show my meetings this day
        """
         :return:
         """
        pass

    def weekly_report(self):  # todo: show my meetings this week
        """
        :return:
        """
        pass

    def Reset_User(self):
        """
               :return:
               """
        pass