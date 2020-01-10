import Sound
import Manager
import RegularUser

#<<<<<<< HEAD
x = RegularUser.Register('a', 'b', '2344', 'abc', '1234')


#print(x.first_name)
#print(x.last_name)
#print(x.id)
#print(x.password)
#print(x.user_name)
#x.add_contact()
x.take_a_photo()
#y = Manager.Manager('E', 'W', 'EE2E2', '2324', '1424','0000')
#=======
#x = Sound.Sound('Amit')
#x.play_record()

"""
# -*- coding: utf-8 -*-

Created on Wed Dec  4 19:08:52 2019

@author: or machlouf
n

import os.path
from os import path

print("Welcome...")
welcome = input("Do you have an acount? y/n: ")

if welcome == "n" or welcome == 'N':
    while True:
        username = input("Enter a username:")
        if path.exists(username + ".txt") == False:
            password = input("Enter a password:")
            password1 = input("Confirm password:")
            Type = input("enter type:")
            if password == password1:
                file = open(username + ".txt", "w")
                file.write(username + ":" + password)
                file.write(username + ":" + Type)
                file.close()
                break
            print("Passwords do NOT match!")
        else:
            print("this username already exist, please try again")

if welcome == "y" or welcome == "Y":
    while True:
        print("\n")
        # print("if you want to exit write: e or E")
        login1 = input("Login:")
        
        if login1=='e' or login1=='E':
            os.remove(username+".txt")
            break
        
        login2 = input("Password:")
        file = open(login1 + ".txt", "r")
        data = file.readline()
        file.close()
        if data == login1 + ":" + login2:
            print("Welcome")
            break
        print("Incorrect username or password.")
        
"""