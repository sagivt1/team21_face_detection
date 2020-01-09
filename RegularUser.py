from Person import Person
from database import DataBase


class RegularUser(Person):
    def __init__(self):
        Person.__init__(self)


    def Register(self):
        # צריך לוודא שלא קיים עוד משתמש במערכת
        Person.Register(self)


    def login(self):
        Person.login(self)

    def my_contacts(self):
        x = self.database.DataBase.get_all_contacts()
        return x

    def daily_report(self):  # todo: show my meetings this day
        """
        Input - none
        Output - report of all the detections in this day
        show a report of all daily detections
        """

        #print("Please enter the day to show the report")
        #self.day = input("Day:")
        #self.month = input(" Month:")
        #self.year = input("Year:")
        #while ((day<1 or day>31) or (month<1 or month>12) or year<1):
          #  print("One or more of the details are invalid,please enter a valid day ")
          #  self.day = input("Day:")
          #  self.month = input(" Month:")
           # self.year = input("Year:")
        #get_detection_by_day(day,month,year)


    def weekly_report(self):  #todo: show my meetings this week
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
"""

    def weekly_report(self):  # todo: show my meetings this week
        """
        Input - none
        Output - report of all the detections in this week
        show a report of all weekly detections
        """

       # print("Please enter the week to show the report")
        #self.day = input("Day:")
        #self.month = input(" Month:")
        #self.year = input("Year:")
       # while ((day<1 or day>31) or (month<1 or month>12) or year<1):
        #    print("One or more of the details are invalid,please enter a valid day ")
        #    self.day = input("Day:")
        #    self.month = input(" Month:")
        #    self.year = input("Year:")
        #get_detection_by_day(day,month,year)


    def monthly_report(self):  # todo: show my meetings this month
        """
         :return:
         """
        pass

    def create_contacts(self):  # todo: create my list contacts
        """
        Input - none
        Output - confirmation message
        delete a contact from the list
        """
        x=database.DataBase.create_contact_list_table(self.user_name)


    def remove_contact(self):  # todo: remove a contact from my list
        """
        Input - none
        Output - confirmation message
        delete a contact from the list
        """
        nick = input("Enter the nick name of the contact you want to remove :")
        x =database.DataBase.remove_contact(self.user_name,nick)
        if x:
            print("The contact was delete ")
        else:
            print("The contact does not exist ")


    def add_contact(self):
        """
         Input - none
         Output - none
         add a new contact to the list
         """
        print("Please enter all the details of your new contact : ")
        first_name = input("First name :")
        last_name = input("Last name :")
        nick = input("Nick name :")
        ##check how to put a pic and sound
        ##img = database.DataBase.update_img_file(first_name, nick, image)
        ##sound = input("sound:")
        img=""
        sound=""
        self.data.insert_new_contact(self.user_name,first_name,last_name,nick)
#,None,None

    def show_contact(self):
        """
        Input - none
        Output - message or show the details of the contact in the list
        show a contact details
        """
        contactnick = input("Nick name of the contact :")
        x = database.DataBase.get_contact(self.user_name,contactnick)
        if x:
            return x
        else:
            print("The contact does not exist ")

    def say_my_contact(self):
        """
        Input - none
        Output - say the name of the contact out loud
        say the name of the contact out loud
        """
        nick = input("Nick name of the contact :")
        database.DataBase.get_sound_contact(self.user_name,nick)


    def delete_my_account(self):
        """
        Input - none
        Output - confirmation message
        delete the account of the user
        """
        database.DataBase.delete_my_account(self.user_name)


    def edit_my_first_name(self):
        self.f_name = input("Enter your new first name :")


    def edit_my_last_name(self):
        self.f_name = input("Enter your new last name :")


    def edit_my_password(self):
        self.passWord = input("Enter your new password :")
        
