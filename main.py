import Sound
import Manager
import RegularUser
import Tester
import datetime
import database
from database import DataBase
import os


def reg():
    manager_code = 24680
    tester_code = 13579
    flag3 = True
    flag4 = True
    while flag4 == True:
        print("Please select one of the following options:")
        print("1. Create manager account")
        print("2. Create tester account")
        print("3. Create regular user account")
        print("4. to exit")
        e = int(input())
        while (e != 1) and (e != 2) and e != 3 and e != 4:
            print("You entered an incorrect number,Please select one of the following options:")
            print("1. Create manager account")
            print("2. Create tester account")
            print("3. Create regular user account")
            print("4. to exit")
            e = int(input())

        if e == 1:
            print('enter manager password:')
            n = int(input())
            if n != manager_code:
                while flag3 == True:
                    while n != manager_code:
                        print("You entered an incorrect code,Please try again:")
                        print("enter manager password:")
                        print("to go back press 2 ")
                        n = int(input())
                        if n == 2:
                            flag3 = False
                            break

            if n == manager_code:
                print("enter first name:")
                fname = input()
                print("enter last name:")
                lname = input()
                print("enter ID")
                id = input()
                print("enter user name:")
                us_name = input()
                print("enter password:")
                password = int(input())
                z = Manager.Manager(fname, lname, id, us_name, password)
                flag4 = False
                main()

        if e == 2:
            print("enter tester code:")
            n = int(input())
            while n != tester_code:
                while flag3 == True:
                    print("You entered an incorrect code,Please try again:")
                    print("enter manager password:")
                    print("to go back press 2 ")
                    n = int(input())
                    if n == 2:
                        flag3 = False
            if n == tester_code:
                print("enter first name:")
                fname = input()
                print("enter last name:")
                lname = input()
                print("enter ID")
                id = input()
                print("enter user name:")
                us_name = input()
                print("enter password:")
                password = int(input())
                y = Tester.Tester(fname, lname, id, us_name, password)
                flag4 = False

        if e == 3:
            print("enter first name:")
            fname = input()
            print("enter last name:")
            lname = input()
            print("enter ID")
            id = input()
            print("enter user name:")
            us_name = input()
            print("enter password:")
            password = int(input())
            x = RegularUser.RegularUser(fname, lname, id, us_name, password)
            flag4 = False

        if e == 4:
            flag4 == False
            main()


def main():
    print("Welcome,")
    print("Please select one of the following options:")
    print("1. Create a new user")
    print("2. Login")
    print("Enter your selection:")
    x = int(input())
    while (1 != x) and (x != 2):
        print("You entered an incorrect number,Please select one of the following options:")
        print("1. Create a new user")
        print("2. Login")
        x = int(input())

    print("")

    if x == 1:
        manager_code = 2468
        tester_code = 13579
        flag3 = True
        flag4 = True
        while flag4 == True:
            print("Please select one of the following options:")
            print("1. Create manager account")
            print("2. Create tester account")
            print("3. Create regular user account")
            print("4. to exit")
            e = int(input())
            print("")
            while (e != 1) and (e != 2) and e != 3 and e != 4:
                print("You entered an incorrect number,Please select one of the following options:")
                print("1. Create manager account")
                print("2. Create tester account")
                print("3. Create regular user account")
                e = int(input())
                print("")
            if e == 1:
                if os.path.isfile("manager.db") != True:
                    print('enter manager code:')
                    n = int(input())
                    if n != manager_code:
                        while flag3 == True:
                            while n != manager_code:
                                print("You entered an incorrect code,Please try again:")
                                print("enter manager code:")
                                print("to go back press 2 ")
                                n = int(input())
                                print("")
                                if n == 2:
                                    flag3 = False
                                    break
                    if n == manager_code:
                        print("enter first name:")
                        fname = input()
                        print("enter last name:")
                        lname = input()
                        print("enter ID")
                        id = input()
                        print("enter user name:")
                        us_name = input()
                        while us_name != "manager":
                            print("Please enter a valid name: manager")
                            us_name = input()
                        print("enter password:")
                        password = int(input())
                        z = Manager.Manager(fname, lname, id, us_name, password)
                        z.create_database()
                        flag4 = False
                        main()
                print("Manager is exists, returns to the menu.")
                print("")
            if e == 2:
                print("enter tester code:")
                n = int(input())
                if n != tester_code:
                    while flag3 == True:
                        while n != tester_code:
                            print("You entered an incorrect code,Please try again:")
                            print("enter tester code:")
                            print("to go back press 2 ")
                            n = int(input())
                            print("")
                            if n == 2:
                                flag3 = False
                                break
                if n == tester_code:
                    print("enter first name:")
                    fname = input()
                    print("enter last name:")
                    lname = input()
                    print("enter ID")
                    id = input()
                    print("enter user name:")
                    us_name = input()
                    print("enter password:")
                    password = int(input())
                    y = Tester.Tester(fname, lname, id, us_name, password)
                    y.create_database()
                    flag4 = False
                    main()
                    print("")

            if e == 3:
                print("enter first name:")
                fname = input()
                print("enter last name:")
                lname = input()
                print("enter ID")
                id = input()
                print("enter user name:")
                us_name = input()
                print("enter password:")
                password = int(input())
                x = RegularUser.RegularUser(fname, lname, id, us_name, password)
                x.create_database()
                flag4 = False
                main()
                print("")

            if e == 4:
                flag4 == False
                print("")
                main()

    if x == 2:
        username = input("enter user name:")
        passwo = input("enter password:")
        print("")
        flg = database.connect(username, passwo)

        while flg is False:
            print("You entered an incorrect user name or password, Please try again")
            username = input("enter user name:")
            passwo = input("enter password")
            print("")
            flg = database.connect(username,passwo)
        ch = database.DataBase(username)
        temp = ch.get_user_info(username)
        ###################################################
        #             regular user  menu                  #
        ###################################################
        if database.get_user_type(username) == "RegularUser":
            user = RegularUser.RegularUser(temp[0][0], temp[0][1], temp[0][2], temp[0][3], temp[0][4])
            print("You have successfully connected to the system!")
            print("")
            flag = True
            while flag != False:
                print("menu:")
                print("To add a contact, press 1.")
                print("To delete a contact, press 2.")
                print("To activate face recognition, press 3.")
                print("To move to reports, press 4.")
                print("To view your contact list, press 5.")
                print("To view a specific contact, press 6.")
                print("To delete your account, press 7.")
                print("To change your name, press 8.")
                print("To Change your last name, press 9.")
                print("To back up your account, press 10.")
                print("To change your password, press 11.")
                print("To view the identification list, press 12.")
                print("To see a list of a specific detection, press 13")
                print("To exit, press 14.")

                print("")
                z = int(input())

                while z != 1 and z != 2 and z != 3 and z != 4 and z != 5 and z != 6 and z != 7 and z != 8 and z != 9 and z != 10 and z != 11 and z != 12 and z != 13 and z!=14:
                    print("You entered an incorrect number,Please select one of the following options:")
                    print("menu:")
                    print("To add a contact, press 1.")
                    print("To delete a contact, press 2.")
                    print("To activate face recognition, press 3.")
                    print("To move to reports, press 4.")
                    print("To view your contact list, press 5.")
                    print("To view a specific contact, press 6.")
                    print("To delete your account, press 7.")
                    print("To change your name, press 8.")
                    print("To Change your last name, press 9.")
                    print("To back up your account, press 10.")
                    print("To change your password, press 11.")
                    print("To view the identification list, press 12.")
                    print("To see a list of a specific detection, press 13")
                    print("To exit, press 14.")
                    print("")
                    z = int(input())
                flag1 = True
                while flag1 != False:
                    if (z == 1):
                        user.add_contact()
                        print("")
                        flag1 = False
                    if (z == 2):
                        user.remove_contact()
                        print("")
                        flag1 = False
                    if (z == 3):
                        user.new_detection()
                        print("")
                        flag1 = False
                    if (z == 4):
                        print("Reports menu:")
                        print("To view the Daily Identification Report, press 1.")
                        print("To view a weekly identification report, press 2.")
                        print("To view the monthly identification report, press 3.")
                        print("To return to the previous menu, press 4.")
                        w = int(input())
                        print("")
                        while w != 1 and w != 2 and w != 3 and w != 4:
                            print("You entered an incorrect number,Please select one of the following options:")
                            print("To view the Daily Identification Report, press 1.")
                            print("To view a weekly identification report, press 2.")
                            print("To view the monthly identification report, press 3.")
                            print("To return to the previous menu, press 4.")
                            print("")
                        if w == 1:
                            user.daily_report()
                            print("")
                            flag1 = False
                        if w == 2:
                            user.weekly_report()
                            print("")
                            flag1 = False
                        if w == 3:
                            user.monthly_report()
                            print("")
                            flag1 = False
                        if w == 4:
                            print("")
                            flag1 = False
                    if z == 5:
                        user.my_contacts()
                        print("")
                        flag1 = False
                    if z == 6:
                        user.show_contact()
                        print("")
                        flag1 = False
                    if z == 7:
                        user.delete_my_account()
                        print("")
                        flag1 = False
                        main()
                    if z == 8:
                        user.edit_my_first_name()
                        print("")
                        flag1 = False
                    if z == 9:
                        user.edit_my_last_name()
                        print("")
                        flag1 = False
                    if z == 10:
                        user.backup()
                        print("The backup is complete")
                        print("")
                        flag1 = False
                    if z == 11:
                        user.edit_my_password()
                        print("")
                        flag1 = False
                    if z == 12:
                        user.show_detection()
                        print("")
                        flag1 = False
                    if z == 13:
                        user.contact_detection()
                        print("")
                        flag1 = False
                    if z == 14:
                        print("")
                        main()

        ###################################################
        #             manager menu                        #
        ###################################################
        if database.get_user_type(username) == "Manager":
            user2 = Manager.Manager(temp[0][0], temp[0][1], temp[0][2], temp[0][3], temp[0][4])
            print("You have successfully connected to the system as Manager!")
            flag = True
            while flag != False:
                print("menu:")
                print("To add a contact, press 1.")
                print("To delete a contact, press 2.")
                print("To activate face recognition, press 3.")
                print("To move to reports, press 4.")
                print("To show specific user, press 5")
                print("To delete a regular user of your choice, press 6.")
                print("To delete a tester user type, press 7.")
                print("To edit user information, press 8.")
                print("To report a bug to the programmer, press 9.")
                print("To exit, press 10.")
                z = int(input())
                while z != 1 and z != 2 and z != 3 and z != 4 and z != 5 and z != 6 and z != 7 and z != 8 and z != 9 and z != 10:
                    print("menu:")
                    print("To add a contact, press 1.")
                    print("To delete a contact, press 2.")
                    print("To activate face recognition, press 3.")
                    print("To move to reports, press 4.")
                    print("To show specific user, press 5")
                    print("To delete a regular user of your choice, press 6.")
                    print("To delete a tester user type, press 7.")
                    print("To edit user information, press 8.")
                    print("To report a bug to the programmer, press 9.")
                    print("To exit, press 10.")
                    z = int(input())
                flag1 = True
                while flag1 != False:
                    if (z == 1):
                        user2.add_contact()
                        flag1 = False
                    if (z == 2):
                        user2.remove_contact()
                        flag1 = False
                    if (z == 3):
                        user2.new_detection()
                        flag1 = False
                    if (z == 4):
                        print("Reports menu:")
                        print("To view registered users, press 1.")
                        print("To return to the previous menu, press 2.")
                        w = int(input())
                        while w != 1 and w != 2:
                            print("You entered an incorrect number,Please select one of the following options:")
                            print("Reports menu:")
                            print("To view registered users, press 1.")
                            print("To return to the previous menu, press 2.")
                            if w == 1:
                                user2.users_amount_report()
                                flag1 = False
                            if w == 2:
                                flag1 = False
                    if z == 5:
                        user2.show_user()
                        flag1 = False
                    if z == 6:
                        print("Enter a username to delete:")
                        f = input()
                        user2.DeleteRegUser(f)
                        flag1 = False
                    if z == 7:
                        print("Enter a username to delete:")
                        f = input()
                        user2.DeleteTester(f)
                        flag1 = False
                    if z == 8:
                        user2.edit_user_details()
                        flag1 = False
                    if z == 9:
                        user2.Report_fail_to_programmer()
                        flag1 = False
                    if z == 10:
                        main()

        ###################################################
        #                 tester menu                     #
        ###################################################
        if database.get_user_type(username) == "Tester":
            user1 = Tester.Tester(temp[0][0], temp[0][1], temp[0][2], temp[0][3], temp[0][4])
            print("You have successfully connected to the system!")
            flag = True
            while flag != False:
                print("menu:")
                print("To add a contact, press 1.")
                print("To delete a contact, press 2.")
                print("To activate face recognition, press 3.")
                print("To move to reports, press 4.")
                print("To view your contact list, press 5.")
                print("To view a specific contact, press 6.")
                print("To delete your account, press 7.")
                print("To change your name, press 8.")
                print("Change your last name, press 9.")
                print("To back up your account, press 10.")
                print("To change your password, press 11.")
                print("To view the identification list, press 12.")
                print("To delete all account information, press 13.")
                print("To add a malfunction, press 14.")
                print("To update the fault status, press 15.")
                print("To exit, press 16.")
                z = int(input())

                while z != 1 and z != 2 and z != 3 and z != 4 and z != 5 and z != 6 and z != 7 and z != 8 and z != 9 and z != 10 and z != 11 and z != 12 and z != 13 and z != 14 and z != 15 and z != 16:
                    print("You entered an incorrect number,Please select one of the following options:")
                    print("menu:")
                    print("To add a contact, press 1.")
                    print("To delete a contact, press 2.")
                    print("To activate face recognition, press 3.")
                    print("To move to reports, press 4.")
                    print("To view your contact list, press 5.")
                    print("To view a specific contact, press 6.")
                    print("To delete your account, press 7.")
                    print("To change your name, press 8.")
                    print("Change your last name, press 9.")
                    print("To back up your account, press 10.")
                    print("To change your password, press 11.")
                    print("To view the identification list, press 12.")
                    print("To delete all account information, press 13.")
                    print("To add a malfunction, press 14.")
                    print("To update the fault status, press 15.")
                    print("To exit, press 16.")
                    z = int(input())
                flag1 = True
                while flag1 != False:
                    if (z == 1):
                        user1.add_contact()
                        flag1 = False
                    if (z == 2):
                        user1.remove_contact()
                        flag1 = False
                    if (z == 3):
                        user1.new_detection()
                        flag1 = False
                    if (z == 4):
                        print("To view the Daily Identification Report, press 1.")
                        print("To view a weekly identification report, press 2.")
                        print("To view the monthly identification report, press 3.")
                        print("To view the fault report, press 4.")
                        print("To view the urgent fault report, press 5.")
                        print("To return to the previous menu, press 6.")
                        w = int(input())
                        while w != 1 and w != 2 and w != 3 and w != 4:
                            print("You entered an incorrect number,Please select one of the following options:")
                            print("To view the Daily Identification Report, press 1.")
                            print("To view a weekly identification report, press 2.")
                            print("To view the monthly identification report, press 3.")
                            print("To view the fault report, press 4.")
                            print("To view the urgent fault report, press 5.")
                            print("To return to the previous menu, press 6.")
                        if w == 1:
                            user1.daily_report()
                            flag1 = False
                        if w == 2:
                            user1.weekly_report()
                            flag1 = False
                        if w == 3:
                            user1.monthly_report()
                            flag1 = False
                        if w == 4:
                            user1.report_of_problems()
                            flag1 = False
                        if w == 5:
                            user1.report_of_urgent_problems()
                            flag1 = False
                        if w == 6:
                            flag1 = False
                    if z == 5:
                        user1.my_contacts()
                        flag1 = False
                    if z == 6:
                        user1.show_contact()
                        flag1 = False
                    if z == 7:
                        user1.delete_my_account()
                        flag1 = False
                    if z == 8:
                        user1.edit_my_first_name()
                        flag1 = False
                    if z == 9:
                        user1.edit_my_last_name()
                        flag1 = False
                    if z == 10:
                        user1.backup()
                        flag1 = False
                    if z == 11:
                        user1.edit_my_password()
                        flag1 = False
                    if z == 12:
                        user1.show_detection()
                        flag1 = False
                    if z == 13:
                        user1.Reset_User()
                        flag1 = False
                    if z == 14:
                        user1.add_fail()
                        flag1 = False
                    if z == 15:
                        user1.update_fail_status()
                        flag1 = False
                    if z == 16:
                        main()


main()
