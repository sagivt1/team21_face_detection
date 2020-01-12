from Person import Person
import Sound
import database
# import face_recognition as fr
import os
# import cv2
# import face_recognition
import numpy as np
from time import sleep
# from cv2 import *
import time
import os.path
import shutil
from datetime import date


class Tester(Person):
    encoded = {}

    def __init__(self, first_name, last_name, i_d, user_name, password):
        super(Tester, self).__init__(first_name, last_name, i_d, user_name, password)

    def create_database(self):
        """
        Input - none
        Output - none
        create tables for Tester user
        """
        self.data.create_user_info_table(self.first_name, self.last_name, self.i_d, self.user_name, self.password)
        self.data.create_detection_table(self.user_name)
        self.data.create_contact_list_table(self.user_name)
        self.data.create_fail_list(self.user_name)
        self.data.create_var_table(self.user_name)

    def report_of_problems(self):  # todo: create a file with problems
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
               Input - None
               Output - None
               show a report of all daily detections
        """
        """print("Enter date you want to get a report")
        day = int(input("Day - "))
        month = int(input('Month - '))
        year = int(input('Year - '))
        while (day < 1 or day > 31) or (month < 1 or month > 12) or (year < 1 or year > 2020):
            print("One or more of the details are invalid,please enter a valid day ")
            day = input("Day:")
            month = input(" Month:")
            year = input("Year:")
        self.data.get_detection_by_day(self.data, day, month, year)"""

    def weekly_report(self):  # todo: show my meetings this week
        """
        Input - none
        Output - report of all the detections in this week
        show a report of all weekly detections
        """
        '''
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
        '''

    def Reset_User(self):
        """
               :return:
               """
        pass

    def my_contacts(self):
        """
        Input - None
        Output - list of contacts
        return all my contacts
        """
        x = self.data.get_all_contacts(self.user_name)
        for i in x:
            print(i)

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
        sound = Sound.Sound(nick)
        self.data.insert_new_contact(self.user_name, first_name, last_name, nick, None, sound.file_path)

    def remove_contact(self):
        """
        Input - None
        Output - None
        delete a contact from the contact list
        """
        nick = input("Enter the nick name of the contact you want to remove :")
        if self.data.remove_contact(self.user_name, nick):
            print("Contact deleted")
        else:
            print("Contact does not exists")

    def show_contact(self):
        """
        Input - none
        Output - message or show the details of the contact in the list
        show a contact details
        """
        contact = input("Nick name of the contact :")
        x = self.data.get_contact(self.user_name, contact)
        if x:
            return x
        else:
            print("The contact does not exist ")

    def delete_my_account(self):
        """
        Input - none
        Output - confirmation message
        delete the account of the user
        """
        self.data.delete_database(self.user_name)

    def edit_my_first_name(self):
        """
        Input - None
        Output - None
        update user first name
        """
        self.first_name = input("Enter your new first name :")
        if self.data.update_first_name(self.user_name, self.first_name):
            print("First name updated")
        else:
            print("First name not updated")

    def edit_my_last_name(self):
        """
        Input - None
        Output - None
        update user last name
        """
        self.last_name = input("Enter your new last name :")
        if self.data.update_last_name(self.user_name, self.last_name):
            print("Last name updated")
        else:
            print("Last name not updated")

    def edit_my_password(self):
        """
        Input - None
        Output - None
        update user password
        """
        self.password = input("Enter your new password :")
        if self.data.update_password(self.user_name, self.password):
            print("Password updated")
        else:
            print("Password not updated")

    def add_fail(self):
        """
        Input - none
        Output - none
        Add new fail to database
        """
        today = date.today()
        fail_name = input("Give a short describe of the fail : ")
        fail_description = input("Full details : ")
        self.data.add_fail(self.user_name, today.day, today.month, today.year, fail_name, fail_description, 0)

    def update_fail_status(self):  # todo: update the status by choice the serial number of the fail
        """
        Input - none
        Output - none
        Update a fail status
        """
        serial = input("enter fail's serial number: ")
        update = input("enter updated fail's status:")
        self.data.update_status(self.user_name, serial, update)

