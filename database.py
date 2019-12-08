import sqlite3


class DataBase:
    def __init__(self):
        '''
        Input - none
        Output - none
        Create a new database to the user with 1 table of contact_list
        '''
        con = sqlite3.connect('my_data')
        con.execute(''' CREATE TABLE IF NOT EXISTS contact_list(
        NICK_NAME PRIMARY KEY TEXT NOT NULL,
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL
        ) ''')
        self.con.close()

    def insert_new_contact(self, first_name, last_name, nick):
        '''
        Input - first name,last name ,nick name all of the type string
        Output - none
        Insert a new contact to table of contact list
        '''
        con = sqlite3.connect('my_data')
        con.execute(''' INSERT INTO contact_list(NICK_NAME,FIRST_NAME,LAST_NAME)
        VALUES(:NICK_NAME,:FIRST_NAME,:LAST_NAME)''',
                    {"NICK_NAME": nick, 'FIRST_NAME': first_name, 'LAST_NAME': last_name})
        con.commit()
        con.close()

    def get_all_contacts(self):
        '''
        Input - none
        Output - contact list information
        Return all the contacts
        '''
        con = sqlite3.connect('my_data')
        data = con.execute(''' select NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list ORDER BY FIRST_NAME ''')
        return data

    def get_contact(self,nick):#todo: create a method that return specific contact details
        '''
        Input - contact nick name of the type string
        Output - return none if not found
        Return a specific contact
        '''
        None

    def remove_contact(self,nick):#todo: create a methods that remove a specific contact
        '''
        Input - nick name of the type string
        Output - True or False if success
        Remove a specific contact
        '''
        None

    def update(self):#todo:create a method that update a specific contact
        '''
        Input - nick name of the type
        Output - True or False if success
        Update a specific contact
        '''