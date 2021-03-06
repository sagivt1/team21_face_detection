from Person import Person
import database
import os


class Manager(Person):
    def __init__(self, first_name, last_name, i_d, user_name, password):
        super(Manager, self).__init__(first_name, last_name, i_d, user_name, password)
        self.data = database.DataBase('manager')

    def create_database(self):
        """
        Input - none
        Output - none
        create tables for Manager
        """
        self.data.create_user_info_table(self.first_name, self.last_name, self.i_d, 'manager', self.password)
        self.data.create_var_table("manager", 'Manager')
        self.data.create_fail_list("manager")
        self.data.create_backup_table("manager")

    def report_of_problems(self):
        x = self.data.get_fails('manager')
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

    def get_backup_user(self):
        """
        Input - None
        Output - None
        show all the user who made backup
        """
        x = self.data.get_users("manager")
        return x

    def show_user(self):
        """
        Input - None
        Output - None
        show details of specific user
        """
        print('Select user name to watch his data')
        x = self.get_backup_user()
        i = 1
        option = []
        for temp in x:
            print(f'{i}.{temp[0]}')
            i += 1
            option.append(temp[0])
        user = input()
        if user not in option:
            print("User is not exists")
            return
        print('Select one of the following option:')
        print('1.User information\n2.Contact list\n3.Detection')
        option = int(input())
        while option not in (1, 2, 3,):
            print('Invalid Option')
            print('Select one of the following option:')
            print('1.User information\n2.Contact list\n3.Detection')
            option = int(input())
        if option == 1:
            check = self.data.get_user_info(user)
            print(f'First name - {check[0][0]}\nLast name - {check[0][1]}\nID - {check[0][2]}\n'
                  f'User name - {check[0][3]}\nPassword - {check[0][4]}')
        if option == 2:
            check = self.data.get_all_contacts(user)
            i = 1
            for temp in check:
                print(f'{i}.{temp[0].title()} {temp[2].title()} Know as - {temp[1].title()} ')
                i += 1
        if option == 3:
            check = self.data.get_detection(user)
            if check:
                for temp in check:
                    print(f'{temp[0]}.{temp[4]} {temp[1]}/{temp[2]}/{temp[3]}')
            else:
                print("There are no detections\n")

    def DeleteRegUser(self, reg):
        self.data.delete_database(reg)
        print("User has been remove")

    def DeleteTester(self, test):
        self.data.delete_database(test)
        print("User has been remove")

    def edit_user_details(self):
        print('Select user name to watch his data')
        x = self.get_backup_user()
        i = 1
        option = []
        for temp in x:
            print(f'{i}.{temp[0]}')
            i += 1
            option.append(temp[0])
        user = input()
        if user not in option:
            print("User is not exists")
            return
        choice = int(input(
            "please select the detail you'd like to edit:\n 1.first name\n 2.last name: \n 3.user name \n 4.ID \n "
            "5.password\n 9.exit\n"))
        while choice not in (1, 2, 3, 4, 9):
            choice = int(input(
                "please select the detail you'd like to edit:\n 1.first name\n 2.last name: \n 3.ID \n 4.password \n "
                "9.exit\n"))
        if choice == 1:
            first_name = input("Enter user's new first name :")
            if self.data.update_first_name(user, first_name):
                print("First name updated")
            else:
                print("First name not updated")
        if choice == 2:
            last_name = input("Enter user's new last name :")
            if self.data.update_last_name(user, last_name):
                print("Last name updated")
            else:
                print("Last name not updated")
        if choice == 3:
            i_d = input("Enter user's new user name :")
            if self.data.update_id(user, i_d):
                print("id updated")
            else:
                print("id not updated")
        if choice == 4:
            password = input("Enter user's new password :")
            if self.data.update_password(user, password):
                print("Password updated")
            else:
                print("Password not updated")
        if choice == 9:
            return

    def users_amount_report(self):
        x = self.data.get_users("manager")
        if x:
            for i in x:
                check = self.data.get_user_info(i[0])
                print(
                    f'First name - {check[0][0]}\nLast name - {check[0][1]}\nID - {check[0][2]}\n'f'User name - {check[0][3]}\n')
            print("total of", len(x), "users", end=" ")
        else:
            print("There are no users who made backup!!")


