from Person import Person
import database


class Tester(Person):
    def __init__(self, f_name, l_name, ID, user, passWord):
        Person.__init__(self, f_name, l_name, ID, user, passWord)

    def Register(self, code):
        if code == '1111':
            Person.register()
            self.data.create_detection_table(self.user_name)
            self.data.create_contact_list_table(self.user_name)
            self.data.create_fail_list(self.user_name)





    def Login(self): self.Login(Person)
