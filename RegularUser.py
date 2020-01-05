from Person import Person
import database


class RegularUser(Person):
    def __init__(self, f_name, l_name, ID, user, passWord):
        Person.__init__(self, f_name, l_name, ID, user, passWord)

        """self.data = database.DataBase()"""

    def Register(self): self.Register(Person)

    def Login(self): self.Login(Person)

    def my_contacts(self):  # todo: list of my contacts
        x = self.database.DataBase.get_all_contacts()
        return x

    def daily_report(self):  # todo: show my meetings this day
        """
        Input - none
        Output - report of all the detections in this day
        show a report of all daily detections
        """
        print("Please enter the day to show the report")
        self.day = input("Day:")
        self.month = input(" Month:")
        self.year = input("Year:")
        while ((day<1 or day>31) or (month<1 or month>12) or year<1):
            print("One or more of the details are invalid,please enter a valid day ")
            self.day = input("Day:")
            self.month = input(" Month:")
            self.year = input("Year:")
        get_detection_by_day(day,month,year)


    def weekly_report(self):  # todo: show my meetings this week
         """
        Input - none
        Output - report of all the detections in this week
        show a report of all weekly detections
        """
        '''
        print("Please enter the week to show the report")
        self.day = input("Day:")
        self.month = input(" Month:")
        self.year = input("Year:")
        while ((day<1 or day>31) or (month<1 or month>12) or year<1):
            print("One or more of the details are invalid,please enter a valid day ")
            self.day = input("Day:")
            self.month = input(" Month:")
            self.year = input("Year:")
        get_detection_by_day(day,month,year)
        '''

    def monthly_report(self):  # todo: show my meetings this month
        """
         :return:
         """
        pass

    def create_contacts(self):  # todo: create my list contacts
        x=self.database.create_contact_list_table()
        return x

    def remove_contact(self, nick):  # todo: remove a contact from my list
        x = self.data.remove_contact(nick)
        return x

    def add_contact(self):  # todo: add a contact to my list
        """
         Input - none
         Output - add a new contact to the list
         add a new contact
         """
        print("Please enter all the details of your new contact : ")
        self.first_name = input("First name :")
        self.last_name = input(" Last name :")
        self.nick = input("Nick name :")
        '''add pic and sound???'''
        x = self.database.DataBase.insert_new_contact(self,first_name, last_name, nick, img, sound)
        return x

    def show_contact(self,contactnick):  # todo: show a contact details
        """
        Input - none
        Output - show the details of the contact in the list
        show a contact details
        """
        x = self.database.get_contact(self,contactnick)
        return x

    def say_my_contact(self):  # todo: say my contact's name out loud
        """
                :return:
                """
        pass

    def delete_my_account(self):  # todo: delete all user's information and delete his account
        """
                :return:
                """
        pass

    def edit_my_first_name(self, new_name):
        self.f_name = new_name

    def edit_my_last_name(self, new_name):
        self.l_name = new_name



    def edit_my_password(self, new_pass):
        self.passWord = new_pass
        return new_pass