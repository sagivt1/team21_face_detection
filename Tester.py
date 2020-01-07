from Person import Person
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

encoded = {}

enter_name = input("entre the name of the person:")


class Tester(Person):
    def __init__(self, f_name, l_name, ID, user, passWord):
        Person.__init__(self, f_name, l_name, ID, user, passWord)

    def Register(self, code):
        if code == '1111':
            Person.register()
            self.data.create_detection_table(self.user_name)
            self.data.create_contact_list_table(self.user_name)
            self.data.create_fail_list(self.user_name)

    def Login(self):
        self.Login(Person)

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
    #             encoded[f.split(".")[i]] = fr.face_encodings(fr.load_image_file("faces/" + f))[i]

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
