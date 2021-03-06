from Person import Person
import database
import Sound
import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
from cv2 import *
import time
import os.path
import shutil
import datetime


class Tester(Person):
    encoded = {}

    def __init__(self, first_name, last_name, i_d, user_name, password):
        super(Tester, self).__init__(first_name, last_name, i_d, user_name, password)
        self.data = database.DataBase(self.user_name)

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
        self.data.create_var_table(self.user_name, "Tester")

    def report_of_problems(self):
        x = self.data.get_fails(self.user_name)
        for i in x:
            print(f'{i[0]}.{i[4]}')
        print('Chose the problem that you want')
        choice = int(input()) - 1
        while choice not in range(0, len(x)):
            print('Invalid choice try again: ')
            choice = int(input()) - 1
        print(f'{x[choice][4].capitalize()}. {x[choice][1]}.{x[choice][2]}.{x[choice][3]}')
        print(f'Status - {x[choice][6]}')
        print('Description:')
        print(f'{x[choice][5].capitalize()}')

    def report_of_urgent_problems(self):
        x = self.data.get_fails(self.user_name)
        option = []
        for i in x:
            if i[6] == 'urgent':
                print(f'{i[0]}.{i[4]}')
                option.append(i[0])
        print('Chose the problem that you want')
        choice = int(input())
        while choice not in option:
            print('Invalid choice try again: ')
            choice = int(input())
        choice -= 1
        print(f'{x[choice][4].capitalize()}. {x[choice][1]}.{x[choice][2]}.{x[choice][3]}')
        print(f'Status - {x[choice][6]}')
        print('Description:')
        print(f'{x[choice][5].capitalize()}')

    def show_contact(self):
        """
        Input - none
        Output - message or show the details of the contact in the list
        show a contact details
        """
        contact = input("Nick name of the contact :")
        x = self.data.get_contact(self.user_name, contact)
        if x:
            print(f'{x[1].capitalize()} {x[2].capitalize()} know as {x[0].capitalize()}')
        else:
            print("The contact does not exist ")

    def daily_report(self):
        """
        Input - None
        Output - None
        show a report of all daily detections
       """
        print("Enter date you want to get a report")
        day = int(input("Day - "))
        month = int(input('Month - '))
        year = int(input('Year - '))
        while (day < 1 or day > 31) or (month < 1 or month > 12) or (year < 1 or year > 2020):
            print("One or more of the details are invalid,please enter a valid day ")
            day = input("Day:")
            month = input("Month:")
            year = input("Year:")
        check = self.data.get_detection_by_day(self.user_name, day, month, year)
        if check:
            for temp in check:
                print(f'{temp[0]} {temp[4].title()}')
        else:
            print("There are no detections")

    def weekly_report(self):
        """
            Input - None
            Output - None
            show a report of week when the last day is the one that the user insert
        """
        count = 0
        print("Please enter the week to show the report")
        Day = int(input("Day:"))
        Month = int(input("Month:"))
        Year = int(input("Year:"))
        cur_year = datetime.date.today().year
        while (Day < 1 or Day > 31) or (Month < 1 or Month > 12) or (Year < 1 or Year > cur_year):
            print("One or more of the details is invalid,please enter a valid date ")
            Day = input("Day:")
            Month = input(" Month:")
            Year = input("Year:")
        date = datetime.date(Year, Month, Day)
        for i in range(0, 7):
            check = self.data.get_detection_by_day(self.user_name, date.day, date.month, date.year)
            if check is not None:
                for temp in check:
                    count += 1
                    print(f'{count}.{temp[4]} {temp[1]}/{temp[2]}/{temp[3]}')
            date = date - datetime.timedelta(days=1)
        if count == 0:
            print("There was not any detection at this week")

    def Reset_User(self):
        """
            input- none
            output- none
            reset user (tester) database and enter new details to open new tester user
         """
        self.data.delete_database(self.user_name)
        print("Please enter your new user information : ")
        first_name = input("First name :")
        last_name = input("Last name :")
        i_d = input("Id :")
        while len(i_d) != 9:
            i_d = input("invalid id ,please enter valid id:")
        user_name = input("user name :")
        password = input("password :")
        self.__init__(first_name, last_name, i_d, user_name, password)
        self.create_database(self.user_name)

    def my_contacts(self):
        """
        Input - None
        Output - list of contacts
        return all my contacts
        """
        x = self.data.get_all_contacts(self.user_name)
        j = 0
        for i in x:
            j += 1
            print(f'{j}.{i[1].capitalize()} {i[2].capitalize()} know as {i[0].capitalize()}')

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
        path = take_a_photo(nick)
        self.data.insert_new_contact(self.user_name, first_name, last_name, nick, path, sound.file_path)

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

    def delete_my_account(self):
        """
        Input - none
        Output - confirmation message
        delete the account of the user
        """
        self.data.delete_database(self.user_name)

    def backup(self):
        self.data.add_backup('manager', self.user_name)

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

    def show_detection(self):
        """
        Input - None
        Output - None
        Show every detection that made
        """
        check = self.data.get_detection(self.user_name)
        if check is not None:
            for temp in check:
                print(f'{temp[0]}.{temp[1]}/{temp[2]}/{temp[3]} - {temp[4]}')
        else:
            print('No detection has made')

    def add_fail(self):
        """
        Input - none
        Output - none
        Add new fail to database
        """
        today = datetime.date.today()
        fail_name = input("Give a short describe of the fail : ")
        fail_description = input("Full details : ")
        self.data.add_fail(self.user_name, today.day, today.month, today.year, fail_name, fail_description, 'open')
        self.data.add_fail('manager', today.day, today.month, today.year, fail_name, fail_description, 'open')

    def update_fail_status(self):
        """
        Input - none
        Output - none
        Update a fail status
        """
        x = self.data.get_fails(self.user_name)
        for i in x:
            print(f'{i[0]}.{i[4]}')
        print('Chose the problem that you want:')
        serial = int(input())
        while serial not in range(1, len(x)+1):
            print('Invalid choice try again: ')
            serial = int(input())
        print('Chose the new status:\n1.Open\n2.Close\n3.Urgent\n')
        update = int(input())
        print(serial)
        while update not in (1, 2, 3):
            print('Invalid option try again!')
            update = int(input())
        if update == 1:
            choice = 'open'
        if update == 2:
            choice = 'close'
        if update == 3:
            choice = 'urgent'
        self.data.update_status(self.user_name, serial, choice)

    def new_detection(self):
        """
        Input - None
        Output - None
        face detection an play the name of the detection
        """
        take_a_test_photo()
        detection_name = classify_face("test.jpg")
        contact = self.data.get_contact(self.user_name, detection_name)
        x = datetime.datetime.now()
        if contact is None:
            Sound.play_record("Sound/Unknown.wav")
        else:
            self.data.add_detection(self.user_name, x.day, x.month, x.year, detection_name)
            Sound.play_record(contact[4])

    def monthly_report(self):
        """
            Input - none
            Output - report of all the detections in this month
            show a report of all weekly detections
        """
        count = 0
        print("Please enter the Month to show the report")
        Day = int(input("Day:"))
        Month = int(input("Month:"))
        Year = int(input("Year:"))
        cur_year = datetime.date.today().year
        while (Day < 1 or Day > 31) or (Month < 1 or Month > 12) or (Year < 1 or Year > cur_year):
            print("One or more of the details is invalid,please enter a valid date ")
            Day = input("Day:")
            Month = input(" Month:")
            Year = input("Year:")
        date = datetime.date(Year, Month, Day)
        for i in range(0, 30):
            check = self.data.get_detection_by_day(self.user_name, date.day, date.month, date.year)
            if check is not None:
                for temp in check:
                    count += 1
                    print(f'{count}.{temp[4]} {temp[1]}/{temp[2]}/{temp[3]}')
            date = date - datetime.timedelta(days=1)
        if count == 0:
            print("There was not any detection at this week")


"""
Face detection section
"""


def take_a_photo(contact_name):
    camera_port = 0
    x = input("To take a picture press Y - ")
    while x.upper() != 'Y':
        x = input("To take a picture press Y - ")
    print('...SMILE...')
    camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
    time.sleep(1)  # If you don't wait, the image will be dark
    return_value, create = camera.read()
    path = "Faces/" + contact_name + ".jpg"
    cv2.imwrite(path, create)
    camera.release()
    cv2.destroyAllWindows()
    del camera  # so that others can use the camera as soon as possible
    return path


def take_a_test_photo():
    camera_port = 0
    x = input("To take a picture press Y - ")
    while x.upper() != 'Y':
        x = input("To take a picture press Y - ")
    print('...SMILE...')
    camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
    time.sleep(1)  # If you don't wait, the image will be dark
    return_value, create = camera.read()
    path = r"test.jpg"
    cv2.imwrite(path, create)
    camera.release()
    cv2.destroyAllWindows()
    del camera  # so that others can use the camera as soon as possible


# def move_photo():
#     source = r"C:\Users\or machlouf\Desktop\face_rec"
#     destination = r"C:\Users\or machlouf\Desktop\face_rec\faces"
#     if not os.path.exists(destination):
#         os.makedirs(destination)
#     for f in os.listdir(source):
#         if f.endswith(enter_name + ".jpg"):
#             shutil.move(os.path.join(source, f), destination)


def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./Faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("Faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("Faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    # img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    # img = img[:,:,::-1]

    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Draw a box around the face
            cv2.rectangle(img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(img, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left - 20, bottom + 15), font, 1.0, (255, 255, 255), 2)

    return name
