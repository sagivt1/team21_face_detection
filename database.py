import sqlite3
import os
from datetime import date


class DataBase:
    def __init__(self, first_name, last_name, i_d, user_name, password):
        """
        Input - none
        Output - none
        Create a new database to the user with 1 table of user info
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute(''' CREATE TABLE IF NOT EXISTS user_info(
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL,
        ID TEXT NOT NULL,
        USER_NAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL 
        ) ''', )
        con.execute(''' INSERT INTO user_info(FIRST_NAME,LAST_NAME,ID,USER_NAME,PASSWORD)
         VALUES(?,?,?,?,?)''', (first_name, last_name, i_d, user_name, password))
        con.commit()
        con.close()

    def create_contact_list_table(self, user_name):

        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute(''' CREATE TABLE IF NOT EXISTS contact_list(
        NICK_NAME TEXT PRIMARY KEY  NOT NULL,
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL
        ) ''')
        con.close()

    def connect(self, user_name, password):
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT USER_NAME,PASSWORD FROM user_info''')
        check = data.fetchone()
        if check[0] == user_name and check[1] == password:
            return True
        else:
            return False

    def insert_new_contact(self, user_name, first_name, last_name, nick):
        """
        Input - first name,last name ,nick name all of the type string
        Output - none
        Insert a new contact to table of contact list
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute(''' INSERT INTO contact_list(NICK_NAME,FIRST_NAME,LAST_NAME)
        VALUES(?,?,?)''', (nick, first_name, last_name))
        con.commit()
        con.close()

    def get_all_contacts(self, user_name):
        """
        Input - none
        Output - contact list information
        Return all the contacts
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list ORDER BY FIRST_NAME ''')
        check = data.fetchall()
        con.close()
        return check

    def get_contact(self, user_name, nick):
        """
        Input - contact nick name of the type string
        Output - return none if not found
        Return a specific contact
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list WHERE NICK_NAME = :NICK_NAME
        ''', {'NICK_NAME': nick})
        check = data.fetchone()
        con.close()
        if not check:
            return None
        else:
            return check

    def remove_contact(self, user_name, nick):
        """
        Input - nick name of the type string
        Output - True or False is success
        Remove a specific contact
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list WHERE NICK_NAME = :NICK_NAME
                ''', {'NICK_NAME': nick})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' DELETE FROM contact_list WHERE NICK_NAME = :NICK_NAME
                        ''', {'NICK_NAME': nick})
            con.commit()
            con.close()
            return True

    def update_nick_name(self, user_name, nick, new_nick):
        """
        Input - nick name and new nick name of the type string
        Output - True or False is success
        Update a specific contact nick name
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list WHERE NICK_NAME = :NICK_NAME
                        ''', {'NICK_NAME': nick})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' UPDATE contact_list SET NICK_NAME = :NICK_NAME_NEW WHERE NICK_NAME = :NICK_NAME
            ''', {'NICK_NAME_NEW': new_nick, 'NICK_NAME': nick})
            con.commit()
            con.close()
            return True

    def update_first_name(self, user_name, nick, first_name):
        """
        Input - nick name and new first name of the type string
        Output - True or False is success
        Update a specific contact first name
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list WHERE NICK_NAME = :NICK_NAME
                        ''', {'NICK_NAME': nick})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' UPDATE contact_list SET FIRST_NAME = :FIRST_NAME WHERE NICK_NAME = :NICK_NAME
            ''', {'FIRST_NAME': first_name, 'NICK_NAME': nick})
            con.commit()
            con.close()
            return True

    def update_last_name(self, user_name, nick, last_name):
        """
        Input - nick name and new first name of the type string
        Output - True or False is success
        Update a specific contact first name
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list WHERE NICK_NAME = :NICK_NAME
                           ''', {'NICK_NAME': nick})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' UPDATE contact_list SET LAST_NAME = :LAST_NAME WHERE NICK_NAME = :NICK_NAME
               ''', {'LAST_NAME': last_name, 'NICK_NAME': nick})
            con.commit()
            con.close()
            return True

    def delete_database(self, user_name):
        db_name = user_name + ".db"
        os.remove(db_name)

    # def create_day_date_table(self):
    #     """
    #     Input - none
    #     Output - none
    #     create a new table of the date for face detection
    #     """
    #     con = sqlite3.connect('my_data')
    #     today = date.today()
    #     con.execute(''' CREATE TABLE IF NOT EXISTS :table_name
    #     TIME TEXT PRIMARY KEY NOT NULL
    #     NICK_NAME TEXT NOT NULL
    #     ''', {'table_name': today.strftime("%m/%d/%y")})
    #     con.close()

    # def insert_detection(self, nick_name):
    #     """
    #     Input - nick name of the detection by the type of string
    #     Output - none
    #     insert new detection
    #     """
    #     con = sqlite3.connect('my_data')
    #     today = date.today()
    #     con.execute(''' INSERT INTO :table_name(TIME,NICK_NAME)
    #      VALUES(:table_name,:NICK_NAME)
    #      ''', {'table_name': today.strftime("%m/%d/%y"), 'NICK_NAME': nick_name})
    #     con.commit()
    #     con.close()
