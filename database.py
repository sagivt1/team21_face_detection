import sqlite3


class DataBase:
    def __init__(self):
        '''
        Create a new database to the user with 1 table of contact_list
        '''
        self.con = sqlite3.connect('my_data')
        self.con.execute(''' CREATE TABLE IF NOT EXISTS contact_list(
        NICK_NAME PRIMARY KEY TEXT NOT NULL,
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL
        ) ''')
        self.con.close()

    def insert_new_contact(self, first_name, last_name, nick):
        '''
        Insert a new contact to table of contact list
        '''
        self.con = sqlite3.connect('my_data')
        self.con.execute(''' INSERT INTO contact_list(NICK_NAME,FIRST_NAME,LAST_NAME)
        VALUES(:NICK_NAME,:FIRST_NAME,:LAST_NAME)''',
                    {"NICK_NAME": nick, 'FIRST_NAME': first_name, 'LAST_NAME': last_name})
        self.con.commit()
        self.con.close()


