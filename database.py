import sqlite3
import os
from datetime import date


class DataBase:
    count_of_detection = 0
    count_of_fails = 0

    def __init__(self, first_name, last_name, i_d, user_name, password):
        """
        Input - first_name, last_name, i_d, user_name, password
        Output - none
        Create a new database to the user with 1 table of user info
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute(''' CREATE TABLE IF NOT EXISTS user_info(
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL,
        ID TEXT NOT NULL,
        USER_NAME TEXT PRIMARY KEY NOT NULL,
        PASSWORD TEXT NOT NULL 
        ) ''', )
        con.execute(''' INSERT INTO user_info(FIRST_NAME,LAST_NAME,ID,USER_NAME,PASSWORD)
         VALUES(?,?,?,?,?)''', (first_name, last_name, i_d, user_name, password))
        con.commit()
        con.close()

    def create_contact_list_table(self, user_name):
        """
        Input - user_name
        Output - None
        create new table of contact list
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute(''' CREATE TABLE IF NOT EXISTS contact_list(
        NICK_NAME TEXT PRIMARY KEY  NOT NULL,
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL,
        IMG TEXT ,
        SOUND TEXT 
        ) ''')
        con.close()

    def create_detection_table(self, user_name):
        """
        Input - user_name
        Output - None
        create new table of detection list
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute('''CREATE TABLE IF NOT EXISTS detection_list(
        SERIAL INT PRIMARY KEY NOT NULL,
        DAY INT NOT NULL,
        MONTH INT NOT NULL,
        YEAR INT NOT NULL,
        NAME TEXT NOT NULL
        )''')
        con.close()

    def create_fail_list(self, user_name):
        """
        Input - user_name
        Output - None
        create a new table of fails
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute('''CREATE TABLE IF NOT EXISTS fail_list(
        SERIAL INT PRIMARY KEY NOT NULL,
        DAY INT NOT NULL,
        MONTH INT NOT NULL,
        YEAR INT NOT NULL,
        FAIL_NAME TEXT NOT NULL,
        FAIL_DESCRIPTION TEXT NOT NULL,
        STATUS INT NOT NULL
        )''')

    def add_fail(self, user_name, day, month, year, fail_name, fail_description, status):
        """
        Input - user name,date of day,month,year,fail name and description ,status 0 - in progress 1 - done
        Output - None
        add new fail to the database
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute('''INSERT INTO fail_list(SERIAL,DAY,MONTH,YEAR,FAIL_NAME,FAIL_DESCRIPTION,STATUS)
                VALUES(?,?,?,?,?,?,?,?,?)''',
                    (DataBase.count_of_fails, day, month, year, fail_name, fail_description, status))
        DataBase.count_of_fails += 1
        con.commit()
        con.close()

    def get_fails(self, user_name):
        """
        Input - user name
        Output - a list of all the fails
        get a list of all the fails
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM fail_list ORDER BY SERIAL''')
        check = data.fetchall()
        con.close()
        return check

    def update_status(self, user_name, serial, status):
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT * FROM fail_list WHERE SERIAL = :SERIAL
                               ''', {'SERIAL': serial})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' UPDATE fail_list SET STATUS = :NEW_STATUS WHERE SERIAL = :SERIAL
            ''', {'NEW_STATUS': status, 'SERIAL': serial})
            con.commit()
            con.close()
            return True

    def get_detection(self, user_name):
        """
        Input - user name
        Output - list of all detection
        return a list of all the face defection
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM detection_list ORDER BY SERIAL''')
        check = data.fetchall()
        con.close()
        return check

    def get_detection_by_day(self, user_name, day, month, year):
        """
        Input - user_name ,date of day,month,year
        Output - return report of the day that the user chose
        Return a report of all the face defection in the day
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM detection_list WHERE DAY=:DAY AND 
        MONTH=:MONTH AND YEAR=:YEAR''', {'DAY': day, 'MONTH': month, 'YEAR': year})
        check = data.fetchall()
        con.close()
        if not check:
            return None
        else:
            return check

    def add_detection(self, user_name, day, month, year, name):
        """
        Input - user name, date of day,month,year and detection name
        Output - None
        add new detection to database
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute('''INSERT INTO detection_list(SERIAL,DAY,MONTH,YEAR,NAME)
        VALUES(?,?,?,?,?)''', (DataBase.count_of_detection, day, month, year, name))
        con.commit()
        con.close()
        DataBase.count_of_detection += 1

    def connect(self, user_name, password):
        """
        Input - user_name
        Output - None
        check if user name is exists
        """
        db_name = user_name + ".db"
        if not os.path.isfile(db_name):
            return False
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT USER_NAME,PASSWORD FROM user_info''')
        check = data.fetchone()

        if check[0] == user_name and check[1] == password:
            return True
        else:
            return False

    def insert_new_contact(self, user_name, first_name, last_name, nick, img, sound):
        """
        Input -user_name,first name,last name ,nick name all of the type string
        Output - none
        Insert a new contact to table of contact list
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute(''' INSERT INTO contact_list(NICK_NAME,FIRST_NAME,LAST_NAME,IMG,SOUND)
        VALUES(?,?,?,?,?)''', (nick, first_name, last_name, img, sound))
        con.commit()
        con.close()

    def get_all_contacts(self, user_name):
        """
        Input - user_name
        Output - contact list information
        Return all the contacts
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(
            ''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME,IMG,SOUND FROM contact_list ORDER BY FIRST_NAME ''')
        check = data.fetchall()
        con.close()
        return check

    def get_contact(self, user_name, nick):
        """
        Input - user_name , contact nick name of the type string
        Output - return none if not found
        Return a specific contact
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME,IMG,SOUND FROM contact_list WHERE NICK_NAME = 
        :NICK_NAME''', {'NICK_NAME': nick})
        check = data.fetchone()
        con.close()
        if not check:
            return None
        else:
            return check

    def remove_contact(self, user_name, nick):
        """
        Input -user_name,nick name of the type string
        Output - True or False is success
        Remove a specific contact
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME,IMG,SOUND FROM contact_list WHERE NICK_NAME = :NICK_NAME
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
        Input - user_name , nick name and new nick name of the type string
        Output - True or False is success
        Update a specific contact nick name
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME,IMG,SOUND FROM contact_list WHERE NICK_NAME = :NICK_NAME
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
        Input - user_name , nick name and new first name of the type string
        Output - True or False is success
        Update a specific contact first name
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME,IMG,SOUND FROM contact_list WHERE NICK_NAME = :NICK_NAME
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
        Input - user_name , nick name and new first name of the type string
        Output - True or False is success
        Update a specific contact first name
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME,IMG,SOUND FROM contact_list WHERE NICK_NAME = :NICK_NAME
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

    def update_img_file(self, user_name, nick, img):
        """
        Input - user name,nick name and new file path to picture
        Output - True or False is susses
        update a specific contact img file path
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME,IMG,SOUND FROM contact_list WHERE NICK_NAME = :NICK_NAME
                                   ''', {'NICK_NAME': nick})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' UPDATE contact_list SET IMG = :IMG WHERE NICK_NAME = :NICK_NAME
                       ''', {'IMG': img, 'NICK_NAME': nick})
            con.commit()
            con.close()
            return True

    def update_sound_file(self, user_name, nick, sound):
        """
        Input - user name,nick name and new file path to sound
        Output - True or False is susses
        update a specific contact sound file path
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME,IMG,SOUND FROM contact_list WHERE NICK_NAME = :NICK_NAME
                                           ''', {'NICK_NAME': nick})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' UPDATE contact_list SET SOUND = :SOUND WHERE NICK_NAME = :NICK_NAME
                               ''', {'SOUND': sound, 'NICK_NAME': nick})
            con.commit()
            con.close()
            return True

    def delete_database(self, user_name):
        """
        Input - user_name
        Output - None
        Delete database file
        """
        db_name = user_name + ".db"
        os.remove(db_name)
