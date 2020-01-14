import Sound
import Manager
import RegularUser
import Tester
import datetime
import database


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

    if x == 1:
        print("Please select one of the following options:")
        print("1. Regular user")
        print("2. Tester account")
        print("3. Manager account")
        y = int(input())
        while y is not 1 and y is not 2 and y is not 3:
            print("You entered an incorrect number,Please select one of the following options:")
            print("1. Regular user")
            print("2. Tester account")
            print("3. Manager account")
            y = int(input())
        #if y == 1:

        #if y == 2:

        #if y == 3:

    if x == 2:
        username = input("enter user name:")
        passwo = input("enter password")
        ch = connect(user_name, passwo)
        while ch is False:
            print("You entered an incorrect user name or password, Please try again")
            username = input("enter user name:")
            passwo = input("enter password")
            ch = connect(user_name, passwo)
###################################################
#             regular user  menu                  #
###################################################
            if type(username) == RegularUser.RegularUser.user_name:
                print("You have successfully connected to the system!")
                flag = True
                while flag!=False:
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
                    print("To exit, press 13.")
                    z = int(input())

                    while z != 1 and z != 2 and z != 3 and z != 4 and z != 5 and z != 6 and z != 7 and z != 8 and z != 9 and z != 10 and z != 11 and z != 12 and z != 13:
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
                        print("To exit, press 13.")
                        z = int(input())
                    flag1 = True
                    while flag1 != False:
                        if (z == 1):
                            add_contact()
                        if (z == 2):
                            remove_contact()
                        if (z == 3):
                            new_detection()
                        if (z == 4):
                            print("Reports menu:")
                            print("To view the Daily Identification Report, press 1.")
                            print("To view a weekly identification report, press 2.")
                            print("To view the monthly identification report, press 3.")
                            print("To return to the previous menu, press 4.")
                            w = int(input())
                            while w != 1 and w != 2 and w != 3 and w != 4:
                                print("You entered an incorrect number,Please select one of the following options:")
                                print("To view the Daily Identification Report, press 1.")
                                print("To view a weekly identification report, press 2.")
                                print("To view the monthly identification report, press 3.")
                                print("To return to the previous menu, press 4.")
                            if w == 1:
                                daily_report()
                            if w == 2:
                                weekly_report()
                            if w == 3:
                                monthly_report()
                            if w == 4:
                                flag1=False
                        if z == 5:
                            my_contacts()
                        if z == 6:
                            show_contact()
                        if z==7:
                            delete_my_account()
                        if z==8:
                            edit_my_first_name()
                        if z == 9:
                            edit_my_last_name()
                        if z == 10:
                            add_backup()
                        if z == 11:
                            edit_my_password()
                        if z==12:
                            show_detection()
                        if z ==13 :
                            main()





###################################################
#             manager menu                        #
###################################################
        if type(passwo) == Manager.Manager.password:
                print("You have successfully connected to the system as Manager!")
                flag = True
                while flag != False:
                    print("menu:")
                    print("To add a contact, press 1.")
                    print("To delete a contact, press 2.")
                    print("To activate face recognition, press 3.")
                    print("To move to reports, press 4.")
                    print("To show specific user, press 5")
                    print("To give permissions to another user, press 6.")
                    print("To delete a regular user of your choice, press 7.")
                    print("To delete a tester user type, press 8.")
                    print("To edit user information, press 9.")
                    print("To view registered users, press 10.")
                    print("To report a bug to the programmer, press 11.")
                    print("To exit, press 12.")
                    z = int(input())
                    while z != 1 and z != 2 and z != 3 and z != 4 and z != 5 and z != 6 and z != 7 and z != 8 and z != 9 and z != 10 and z != 11 and z != 12:
                        print("menu:")
                        print("To add a contact, press 1.")
                        print("To delete a contact, press 2.")
                        print("To activate face recognition, press 3.")
                        print("To move to reports, press 4.")
                        print("To show specific user, press 5")
                        print("To give permissions to another user, press 6.")
                        print("To delete a regular user of your choice, press 7.")
                        print("To delete a tester user type, press 8.")
                        print("To edit user information, press 9.")
                        print("To view registered users, press 10.")
                        print("To report a bug to the programmer, press 11.")
                        print("To exit, press 11.")
                        z = int(input())
                    flag1 = True
                    while flag1 != False:
                        if (z == 1):
                            add_contact()
                        if (z == 2):
                            remove_contact()
                        if (z == 3):
                            new_detection()
                        if (z == 4):
                            print("Reports menu:")
                            print("To view the Daily Identification Report, press 1.")
                            print("To view a weekly identification report, press 2.")
                            print("To view the monthly identification report, press 3.")
                            print("To return to the previous menu, press 4.")
                            w = int(input())
                            while w != 1 and w != 2 and w != 3:
                                print("You entered an incorrect number,Please select one of the following options:")
                                print("To view the Daily Identification Report, press 1.")
                                print("To view a weekly identification report, press 2.")
                                print("To view the monthly identification report, press 3.")
                                print("To return to the previous menu, press 4.")
                                if w == 1:
                                    daily_report()
                                if w == 2:
                                    weekly_report()
                                if w == 3:
                                    monthly_report()
                                if w == 4:
                                    flag1 = False
                        if z==5:
                            show_user()
                        if z==6:
                            GivePermission()
                        if z == 7:
                            print("Enter a username to delete:")
                            f = input()
                            DeleteRegUser(f)
                        if z == 8:
                            print("Enter a username to delete:")
                            f = input()
                            DeleteTester(f)
                        if z == 9:
                            edit_user_details()
                        if z == 10:
                            users_amount_report()
                        if z == 11:
                            Report_fail_to_programmer()
                        if z == 12:
                            main()





###################################################
#                 tester menu                     #
###################################################
        if type(passwo) == Tester.Tester.password:
            print("You have successfully connected to the system!")
            flag = True
            while flag != False:
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
                        add_contact()
                    if (z == 2):
                        remove_contact()
                    if (z == 3):
                        new_detection()
                    if (z == 4):
                        print("You entered an incorrect number,Please select one of the following options:")
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
                            daily_report()
                        if w == 2:
                            weekly_report()
                        if w == 3:
                            monthly_report()
                        if z == 4:
                            report_of_problems()
                        if z == 5:
                            report_of_urgent_problems()
                        if w == 6:
                            flag1 = False
                    if z == 5:
                        my_contacts()
                    if z == 6:
                        show_contact()
                    if z == 7:
                        delete_my_account()
                    if z == 8:
                        edit_my_first_name()
                    if z == 9:
                        edit_my_last_name()
                    if z == 10:
                        add_backup()
                    if z == 11:
                        edit_my_password()
                    if z == 12:
                        show_detection()
                    if z == 13:
                        Reset_User()
                    if z == 14:
                        add_fail()
                    if z == 15:
                        update_fail_status()
                    if z == 16:
                        main()

main()

