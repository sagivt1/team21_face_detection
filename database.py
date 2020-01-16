import sqlite3
import os
from datetime import date


def get_user_type(user_name):
    """
    Input - user_name
    Output - user type by string
    return the user type
    """
    db_name = user_name + ".db"
    con = sqlite3.connect(db_name)
    data = con.execute('''SELECT * FROM var ''')
    check = data.fetchall()
    con.close()
    return check[0][2]


def connect(user_name, password):
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
    con.close()
    if check[0] == user_name and check[1] == password:
        return True
    else:
        return False


class DataBase:

    def __init__(self, user_name):
        """
        Input - none
        Output - none
        Create a new database to the user with no tables
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.close()

    def create_backup_table(self, user_name):
        """
        Input - User_name
        Output - None
        create a table that of user that create a database backups
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute(''' CREATE TABLE IF NOT EXISTS backup(
                            USER_NAME TEXT PRIMARY KEY NOT NULL ,
                            PATH TEXT NOT NULL
                               ) ''', )
        con.close()

    def add_backup(self, user_name, add_user_name):
        """
        Input - user_name , add_user_name(the user_name which his data you backup),path to the database
        Output - None
        create a backup to the database
        """
        db_name = user_name + ".db"
        path = add_user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute(''' INSERT INTO backup(USER_NAME,PATH)
                       VALUES(?,?)''', (add_user_name, path))
        con.commit()
        con.close()

    def get_users(self, user_name):
        """
        Input - user name
        Output - list of all detection
        return a list of all the face defection
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM backup ''')
        check = data.fetchall()
        con.close()
        if not check:
            return None
        else:
            return check

    def create_var_table(self, user_name, user_type):
        """
        Input - user_name
        Output - None
        create a table that contain count_of_detection and count_of_fails
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute(''' CREATE TABLE IF NOT EXISTS var(
                    COUNT_OF_DETECTION INT,
                    COUNT_OF_FAILS INT,
                    USER_TYPE TEXT
                       ) ''', )
        con.execute(''' INSERT INTO var(COUNT_OF_DETECTION,COUNT_OF_FAILS,USER_TYPE)
                VALUES(?,?,?)''', (0, 0, user_type))
        con.commit()
        con.close()

    def get_count_of_fails(self, user_name):
        """
        Input - user_name
        Output - countof fails by int
        return the count fails
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM var ''')
        check = data.fetchall()
        con.close()
        return check[0][1]


    def get_count_of_detection(self, user_name):
        """
        Input - user_name
        Output - none
        return the count detection
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM var ''')
        check = data.fetchall()
        con.close()
        return check[0][0]

    def count_one_more_fail(self, user_name):
        """
        Input - noe
        Output - none
        add one more fail to the counter
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM var ''')
        check = data.fetchall()
        con.execute('''UPDATE var SET COUNT_OF_FAILS =:COUNT_OF_FAILS
                        ''', {'COUNT_OF_FAILS': check[0][1] + 1})
        con.commit()
        con.close()

    def count_one_more_detection(self, user_name):
        """
        Input - noe
        Output - none
        add one more detection to the counter
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM var ''')
        check = data.fetchall()
        con.execute('''UPDATE var SET COUNT_OF_DETECTION=:COUNT_OF_DETECTION
                        ''', {'COUNT_OF_DETECTION': check[0][0] + 1})
        con.commit()
        con.close()

    def create_user_info_table(self, first_name, last_name, i_d, user_name, password):
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
        con.execute(''' INSERT INTO user_info(FIRST_NAME,LAST_NAME,ID,USER_NAME,PASSWORD)VALUES(?,?,?,?,?)''',
                    (first_name, last_name, i_d, user_name, password))
        con.commit()
        con.close()

    def get_user_info(self, user_name):
        """
        Input - user_name
        Output - user name information of tuple
        return tuple of the user name information
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM user_info''')
        check = data.fetchall()
        con.close()
        if not check:
            return None
        else:
            return check

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
        IMG TEXT NOT NULL ,
        SOUND TEXT NOT NULL 
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
        con.close()

    def add_fail(self, user_name, day, month, year, fail_name, fail_description, status):
        """
        Input - user name,date of day,month,year,fail name and description ,status 0 - in progress 1 - done
        Output - None
        add new fail to the database
        """
        self.count_one_more_fail(user_name)
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute('''INSERT INTO fail_list(SERIAL,DAY,MONTH,YEAR,FAIL_NAME,FAIL_DESCRIPTION,STATUS)
                VALUES(?,?,?,?,?,?,?)''',
                    (self.get_count_of_fails(user_name), day, month, year, fail_name, fail_description, status))
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

    def get_fails_by_day(self, user_name, day, month, year):
        """
        Input - user_name ,date of day,month,year
        Output - return report of the day that the tester chose
        Return a report of all the fails in the day
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM fail_list WHERE DAY=:DAY AND 
        MONTH=:MONTH AND YEAR=:YEAR''', {'DAY': day, 'MONTH': month, 'YEAR': year})
        check = data.fetchall()
        con.close()
        if not check:
            return None
        else:
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
        if not check:
            return None
        else:
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

    def get_detection_by_nick(self, user_name,nick):
        """
        Input - user_name ,nick name of the contact
        Output - list of all the detection
        Return a list of all the detection of specific ucotact
        """
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute('''SELECT * FROM detection_list WHERE NAME=:NAME '''
                           , {'NAME':nick})
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
        self.count_one_more_detection(user_name)
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        con.execute('''INSERT INTO detection_list(SERIAL,DAY,MONTH,YEAR,NAME)
        VALUES(?,?,?,?,?)''', (self.get_count_of_detection(user_name), day, month, year, name))
        con.commit()
        con.close()

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

    def update_contact_nick_name(self, user_name, nick, new_nick):
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

    def update_contact_first_name(self, user_name, nick, first_name):
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

    def update_contact_last_name(self, user_name, nick, last_name):
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

    def update_contact_img_file(self, user_name, nick, img):
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

    def update_contact_sound_file(self, user_name, nick, sound):
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

    def update_first_name(self, user_name, new_name):
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT * FROM user_info ''')
        check = data.fetchone()
        if not check:
            con.close()
            return False
        con.execute('''UPDATE user_info SET FIRST_NAME=:FIRST_NAME
                            ''', {'FIRST_NAME': new_name})
        con.commit()
        con.close()
        return True

    def update_last_name(self, user_name, new_last):
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT * FROM user_info ''')
        check = data.fetchone()
        if not check:
            con.close()
            return False
        con.execute('''UPDATE user_info SET LAST_NAME=:LAST_NAME
                            ''', {'LAST_NAME': new_last})
        con.commit()
        con.close()
        return True

    def update_user_name(self, user_name, new_user):
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT * FROM user_info ''')
        check = data.fetchone()
        if not check:
            con.close()
            return False
        con.execute('''UPDATE user_info SET USER_NAME=:USER_NAME''', {'USER_NAME': new_user})
        con.commit()
        con.close()
        return True

    def update_id(self, user_name, new_id):
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT * FROM user_info ''')
        check = data.fetchone()
        if not check:
            con.close()
            return False
        con.execute('''UPDATE user_info SET I_D=:I_D
                               ''', {'I_D': new_id})
        con.commit()
        con.close()
        return True

    def update_password(self, user_name, new_pass):
        db_name = user_name + ".db"
        con = sqlite3.connect(db_name)
        data = con.execute(''' SELECT * FROM user_info ''')
        check = data.fetchone()
        if not check:
            con.close()
            return False
        con.execute('''UPDATE user_info SET PASSWORD=:PASSWORD
                               ''', {'PASSWORD': new_pass})
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
        con = sqlite3.connect('manager.db')
        con.execute('''DELETE FROM backup WHERE USER_NAME=:USER_NAME
                                       ''', {'USER_NAME': user_name})
        con.commit()
        con.close()

    def delete_manager_database(self, user_name):
        """
        Input - user_name
        Output - None
        Delete database file
        """
        db_name = user_name + ".db"
        os.remove(db_name)

