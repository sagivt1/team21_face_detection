import unittest
import database


class TestDataBase(unittest.TestCase):

    def test_connect(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_var_table('user')
        flag = data.connect('user', 'password')
        data.delete_database('user')
        self.assertEqual(flag, True)

    def test_insert_and_get(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user')
        data.insert_new_contact('user', 'sagiv', 'talker', 'sagiv', 'None', 'None')
        x = ("sagiv", "sagiv", "talker", 'None', 'None')
        check = data.get_contact('user', "sagiv")
        data.delete_database('user')
        self.assertEqual(check, x)

    def test_get_all_contact(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user')
        data.insert_new_contact('user', 'sagiv', 'talker', 'sagiv', 'None', "None")
        data.insert_new_contact('user', "or", "machlouf", "or", "None", "None")
        x = [("or", "or", "machlouf", "None", "None"), ("sagiv", "sagiv", "talker", "None", "None")]
        check = data.get_all_contacts('user')
        data.delete_database('user')
        self.assertEqual(check, x)

    def test_remove_contact(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user')
        data.insert_new_contact('user', 'sagiv', 'talker', 'sagiv', "None", "None")
        flag = data.remove_contact('user', 'sagiv')
        data.delete_database('user')
        self.assertEqual(flag, True)

    def test_update(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user')
        data.insert_new_contact('user', 'sagiv', 'talker', 'sagiv', "None", "None")
        data.update_contact_last_name('user', 'sagiv', 'c')
        data.update_contact_first_name('user', 'sagiv', 'b')
        data.update_contact_nick_name('user', 'sagiv', 'a')
        data.update_contact_img_file('user', 'a', 'new')
        data.update_contact_sound_file('user', 'a', 'new')
        x = ('a', 'b', 'c', 'new', 'new')
        check = data.get_contact('user', 'a')
        data.delete_database('user')
        self.assertEqual(check, x)

    def test_get_detection_by_day(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user')
        data.create_detection_table('user')
        data.insert_new_contact('user', 'sagiv', 'talker', 'sagiv', "None", "None")
        data.add_detection('user', 1, 1, 2020, 'a')
        data.add_detection('user', 1, 1, 2020, 'a')
        check = data.get_detection_by_day('user', 1, 1, 2020)
        data.delete_database('user')
        x = [(1, 1, 1, 2020, 'a'), (2, 1, 1, 2020, 'a')]
        self.assertEqual(check, x)


if __name__ == '__main__':
    unittest.main()
