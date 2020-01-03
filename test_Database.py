import unittest
import database


class TestDataBase(unittest.TestCase):

    def test_connect(self):
        data = database.DataBase('first', 'last', 'id', 'user', 'password')
        flag = data.connect('user', 'password')
        data.delete_database('user')
        self.assertEqual(flag, True)

    def test_insert_and_get(self):
        data = database.DataBase("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.insert_new_contact('user','sagiv', 'talker', 'sagiv','None','None')
        x = ("sagiv", "sagiv", "talker",'None','None')
        check = data.get_contact('user',"sagiv")
        data.delete_database('user')
        self.assertEqual(check, x)

    def test_get_all_contact(self):
        data = database.DataBase("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.insert_new_contact('user','sagiv', 'talker', 'sagiv','None',"None")
        data.insert_new_contact('user',"or", "machlouf", "or","None","None")
        x = [("or", "or", "machlouf","None","None"), ("sagiv", "sagiv", "talker","None","None")]
        check = data.get_all_contacts('user')
        data.delete_database('user')
        self.assertEqual(check, x)

    def test_remove_contact(self):
        data = database.DataBase("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.insert_new_contact('user','sagiv', 'talker', 'sagiv',"None","None")
        flag = data.remove_contact('user','sagiv')
        data.delete_database('user')
        self.assertEqual(flag, True)

    def test_update(self):
        data = database.DataBase("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.insert_new_contact('user','sagiv', 'talker', 'sagiv',"None","None")
        data.update_last_name('user','sagiv', 'c')
        data.update_first_name('user','sagiv', 'b')
        data.update_nick_name('user','sagiv', 'a')
        data.update_img_file('user','a','new')
        data.update_sound_file('user','a','new')
        x = ('a', 'b', 'c','new','new')
        check = data.get_contact('user','a')
        data.delete_database('user')
        self.assertEqual(check, x)


if __name__ == '__main__':
    unittest.main()
