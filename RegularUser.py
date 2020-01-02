from Person import Person
import database


class RegularUser(Person):
    def __init__(self, f_name, l_name, ID, user, passWord):
        Person.__init__(self, f_name, l_name, ID, user, passWord)

        """self.data = database.DataBase()"""

    def Register(self): self.Register(Person)

    def Login(self): self.Login(Person)

    def my_contacts(self):  # todo: list of my contacts
        x = self.database.DataBase.get_all_contacts()
        return x

    def daily_report(self):  # todo: show my meetings this day

        """
        """
        pass

    def weekly_report(self):  # todo: show my meetings this week

        """
        """
        pass

    def monthly_report(self):  # todo: show my meetings this month
        """
         :return:
         """
        pass

    def create_contacts(self):  # todo: create my list contacts
        """
        :return:
        """
        pass

    def remove_contact(self, nick):  # todo: remove a contact from my list
        x = self.data.remove_contact(nick)
        return x

    def add_contact(self):  # todo: add a contact to my list
        x = self.database.DataBase.insert_new_contact()
        return x

    def show_contact(self):  # todo: show a contact details
        x = self.database.get_all_contacts()
        return x

    def say_my_contact(self):  # todo: say my contact's name out loud
        """
                :return:
                """
        pass

    def delete_my_account(self):  # todo: delete all user's information and delete his account
        """
                :return:
                """
        pass

    def edit_my_first_name(self, new_name):
        self.f_name = new_name

    def edit_my_last_name(self, new_name):
        self.l_name = new_name

    def edit_my_password(self, new_pass):
        self.passWord = new_pass
        return new_pass
