from datetime import date

from Person import Person


class RegularUser(Person):
    def __init__(self):
        Person.__init__(self)

    def Register(self):
        Person.register(self)

    def Login(self):
        Person.login(self)

    def my_contacts(self):
        x = self.data.get_all_contacts()
        return x

    def daily_report(self):  # todo: show my meetings this day
        """
        Input - none
        Output - report of all the detections in this day
        show a report of all daily detections
        """
        print("Please enter the details of the report")
        day = input("Day:")
        month = input(" Month:")
        year = input("Year:")
        while (day < 1 or day > 31) or (month < 1 or month > 12) or (year < 1 or year > 2020):
            print("One or more of the details are invalid,please enter a valid date ")
            day = input("Day:")
            month = input(" Month:")
            year = input("Year:")
        self.data.get_detection_by_day(self.data, self.user_name, day, month, year)

    def weekly_report(self):  # todo: show my meetings this week
        """
        Input - none
        Output - report of all the detections in this week
        show a report of all weekly detections
        """

        print("Please enter the week to show the report")
        day = input("Day:")
        month = input(" Month:")
        year = input("Year:")
        while (day < 1 or day > 31) or (month < 1 or month > 12) or (year < 1 or year > 2020):
            print("One or more of the details are invalid,please enter a valid day ")
            day = input("Day:")
            month = input(" Month:")
            year = input("Year:")
        self.data.get_detection_by_week(self.data, day, month, year)

    def monthly_report(self):  # todo: show my meetings this month
        """
         :return:
         """
        pass

    def create_contacts(self):  # todo: create my list contacts
        x = self.data.create_contact_list_table()
        return x

    def remove_contact(self, nick):  # todo: remove a contact from my list
        x = self.data.remove_contact(nick)
        return x

    def add_contact(self):
        """
         Input - none
         Output - add a new contact to the list
         add a new contact to the list
         """
        print("Please enter all the details of your new contact : ")
        first_name = input("First name :")
        last_name = input(" Last name :")
        nick = input("Nick name :")
        '''add pic and sound???'''
        x = self.data.insert_new_contact(self, first_name, last_name, nick, img, sound)
        return x

    def Delete_contact(self):
        """
         Input - none
         Output - add a new contact to the list
         add a new contact
         """
        print("Please enter all the details of your new contact : ")
        first_name = input("First name :")
        last_name = input(" Last name :")
        nick = input("Nick name :")
        '''add pic and sound???'''
        x = self.data.insert_new_contact(self, first_name, last_name, nick, img, sound)
        return x

    def show_contact(self):
        """
        Input - none
        Output - show the details of the contact in the list
        show a contact details
        """
        contactNick = input("Nick name of the contact :")
        x = self.data.get_contact(self, self.user_name, contactNick)
        return x

    def say_my_contact(self):
        """
        Input - none
        Output - say the name of the contact out loud
        say the name of the contact out loud
        """
        nick = input("Nick name of the contact :")
        self.data.get_sound_contact(self, self.user_name, nick)

    def delete_my_account(self):
        """
        Input - none
        Output - confirmation message
        delete the account of the user
        """
        self.data.delete_database(self, self.user_name)

    def edit_my_first_name(self):
        self.first_name = input("Enter your new first name :")

    def edit_my_last_name(self):
        self.last_name = input("Enter your new last name :")

    def edit_my_password(self):
        self.password = input("Enter your new password :")
