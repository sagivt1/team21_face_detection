import sqlite3


class DataBase:
    def __init__(self):
        """
        Input - none
        Output - none
        Create a new database to the user with 1 table of contact_list
        """
        con = sqlite3.connect('my_data')
        con.execute(''' CREATE TABLE IF NOT EXISTS contact_list(
        NICK_NAME PRIMARY KEY TEXT NOT NULL,
        FIRST_NAME TEXT NOT NULL,
        LAST_NAME TEXT NOT NULL
        ) ''')
        con.close()

    def insert_new_contact(self, first_name, last_name, nick):
        """
        Input - first name,last name ,nick name all of the type string
        Output - none
        Insert a new contact to table of contact list
        """
        con = sqlite3.connect('my_data')
        con.execute(''' INSERT INTO contact_list(NICK_NAME,FIRST_NAME,LAST_NAME)
        VALUES(:NICK_NAME,:FIRST_NAME,:LAST_NAME)''',
                    {"NICK_NAME": nick, 'FIRST_NAME': first_name, 'LAST_NAME': last_name})
        con.commit()
        con.close()

    def get_all_contacts(self):
        """
        Input - none
        Output - contact list information
        Return all the contacts
        """
        con = sqlite3.connect('my_data')
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list ORDER BY FIRST_NAME ''')
        con.close()
        return data

    def get_contact(self, nick):
        """
        Input - contact nick name of the type string
        Output - return none if not found
        Return a specific contact
        """
        con = sqlite3.connect('my_data')
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list WHERE NICK_NAME = :NICK_NAME
        ''', {'NICK_NAME': nick})
        check = data.fetchone()
        con.close()
        if not check:
            return None
        else:
            return data

    def remove_contact(self, nick):
        """
        Input - nick name of the type string
        Output - True or False is success
        Remove a specific contact
        """
        con = sqlite3.connect('my_data')
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

    def update_nick_name(self, nick, new_nick):
        """
        Input - nick name and new nick name of the type string
        Output - True or False is success
        Update a specific contact nick name
        """
        con = sqlite3.connect('my_data')
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list WHERE NICK_NAME = :NICK_NAME
                        ''', {'NICK_NAME': nick})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' UPDATE contact_list SET NICK_NAME = :NICK_NAME_NEW WHERE NICK_NAME = :NICK-NAME
            ''', {'NICK_NAME_NEW': new_nick, 'NICK_NAME': nick})
            con.commit()
            con.close()
            return True

    def update_first_name(self, nick, first_name):
        """
        Input - nick name and new first name of the type string
        Output - True or False is success
        Update a specific contact first name
        """
        con = sqlite3.connect('my_data')
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list WHERE NICK_NAME = :NICK_NAME
                        ''', {'NICK_NAME': nick})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' UPDATE contact_list SET FIRST_NAME = :FIRST_NAME WHERE NICK_NAME = :NICK-NAME
            ''', {'NICK_NAME_NEW': first_name, 'NICK_NAME': nick})
            con.commit()
            con.close()
            return True

    def update_last_name(self, nick, last_name):
        """
        Input - nick name and new first name of the type string
        Output - True or False is success
        Update a specific contact first name
        """
        con = sqlite3.connect('my_data')
        data = con.execute(''' SELECT NICK_NAME,FIRST_NAME,LAST_NAME FROM contact_list WHERE NICK_NAME = :NICK_NAME
                           ''', {'NICK_NAME': nick})
        check = data.fetchone()
        if not check:
            con.close()
            return False
        else:
            con.execute(''' UPDATE contact_list SET FIRST_NAME = :LAST_NAME WHERE NICK_NAME = :NICK-NAME
               ''', {'LAST_NAME': last_name, 'NICK_NAME': nick})
            con.commit()
            con.close()
            return True
