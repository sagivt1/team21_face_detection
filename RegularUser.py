from Person import Person
import database
import Sound
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


class RegularUser(Person):
    def __init__(self, first_name, last_name, i_d, user_name, password):
        super(RegularUser, self).__init__(first_name, last_name, i_d, user_name, password)

    def create_database(self):
        """
        Input - none
        Output - none
        create tables for Regular user
        """
        self.data.create_user_info_table(self.first_name, self.last_name, self.i_d, self.user_name, self.password)
        self.data.create_contact_list_table(self.user_name)
        self.data.create_detection_table(self.user_name)
        self.data.create_var_table(self.user_name)

    def my_contacts(self):
        """
        Input - None
        Output - list of contacts
        return all my contacts
        """
        x = self.data.get_all_contacts(self.user_name)
        for i in x:
            print(i)

    # def move_photo(self):
    #     global encoded
    #     i = 0
    #     source = r"C:\Users\or machlouf\PycharmProjects\new_project"
    #     destination = r"C:\Users\or machlouf\PycharmProjects\new_project\faces"
    #     if not os.path.exists(destination):
    #         os.makedirs(destination)
    #     for f in os.listdir(source):
    #         if f.endswith(enter_name + ".jpg"):
    #             shutil.move(os.path.join(source, f), destination)
    #             encoded[f.split(".")[i]] = fr.face_encodings(fr.load_image_file("Faces/" + f))[i]

    # def take_a_photo(self):
    #     camera_port = 0
    #     camera = cv2.VideoCapture(camera_port)
    #     time.sleep(0.1)  # If you don't wait, the image will be dark
    #     return_value, create = camera.read()
    #     # enter_name = input("entre the name of the person:")
    #     cv2.imwrite(enter_name + ".jpg", create)
    #     del (camera)  # so that others can use the camera as soon as possible

    # def get_encoded_faces():
    #     """
    #     looks through the faces folder and encodes all
    #     the faces
    #
    #     :return: dict of (name, image encoded)
    #     """
    #     encoded = {}
    #     for (dirpath, dnames, fnames) in os.walk("./faces"):
    #         for f in fnames:
    #             i = 0
    #             if f.endswith(".jpg") or f.endswith(".png"):
    #                 print(i)
    #                 face = fr.load_image_file("faces/" + f)
    #                 encoding = fr.face_encodings(face)[i]
    #                 encoded[f.split(".")[i]] = encoding
    #     return encoded

    # def unknown_image_encoded(img):
    #     """
    #     encode a face given the file name
    #     """
    #     face = fr.load_image_file("faces/" + img)
    #     encoding = fr.face_encodings(face)[0]
    #
    #     return encoding

    # def classify_face(im):
    #     """
    #     will find all of the faces in a given image and label
    #     them if it knows what they are
    #
    #     :param im: str of file path
    #     :return: list of face names
    #     """
    #     faces = get_encoded_faces()
    #     faces_encoded = list(faces.values())
    #     known_face_names = list(faces.keys())
    #
    #     img = cv2.imread(im, 1)
    #     img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #     # img = img[:,:,::-1]
    #
    #     face_locations = face_recognition.face_locations(img)
    #     unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
    #
    #     face_names = []
    #     for face_encoding in unknown_face_encodings:
    #         # See if the face is a match for the known face(s)
    #         matches = face_recognition.compare_faces(faces_encoded, face_encoding)
    #         name = "Unknown"
    #
    #         # use the known face with the smallest distance to the new face
    #         face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
    #         best_match_index = np.argmin(face_distances)
    #         if matches[best_match_index]:
    #             name = known_face_names[best_match_index]
    #
    #         face_names.append(name)
    #
    #         for (top, right, bottom, left), name in zip(face_locations, face_names):
    #             # Draw a box around the face
    #             cv2.rectangle(img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)
    #
    #             # Draw a label with a name below the face
    #             cv2.rectangle(img, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 0, 0), cv2.FILLED)
    #             font = cv2.FONT_HERSHEY_DUPLEX
    #             cv2.putText(img, name, (left - 20, bottom + 15), font, 1.0, (255, 255, 255), 2)
    #
    #     # Display the resulting image
    #     while True:
    #
    #         cv2.imshow('Video', img)
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             return face_names

    def daily_report(self):  # todo:report of daily
        """
        Input - None
        Output - None
        show a report of all daily detections
        """
        # print("Enter date you want to get a report")
        # day = int(input("Day - "))
        # month = int(input('Month - '))
        # month = int(input('Year - '))

    def weekly_report(self):  # todo: show my meetings this week
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
    # self.day = input("Day:")
    # self.month = input(" Month:")
    # self.year = input("Year:")
    # while ((day<1 or day>31) or (month<1 or month>12) or year<1):
    #    print("One or more of the details are invalid,please enter a valid day ")
    #    self.day = input("Day:")
    #    self.month = input(" Month:")
    #    self.year = input("Year:")
    # get_detection_by_day(day,month,year)

    def monthly_report(self):  # todo: show my meetings this month
        """
         :return:
         """
        pass

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
