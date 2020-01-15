import unittest
import database


class TestDataBase(unittest.TestCase):

    def test_connect(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_var_table('user', 'RegularUser')
        flag = database.connect('user', 'password')
        data.delete_database('user')
        self.assertEqual(flag, True)

    def test_insert_and_get(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user', 'RegulaUser')
        data.insert_new_contact('user', 'sagiv', 'talker', 'sagiv', 'None', 'None')
        x = ("sagiv", "sagiv", "talker", 'None', 'None')
        check = data.get_contact('user', "sagiv")
        data.delete_database('user')
        self.assertEqual(check, x)

    def test_get_all_contact(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user', 'RegularUser')
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
        data.create_var_table('user', 'RegularUser')
        data.insert_new_contact('user', 'sagiv', 'talker', 'sagiv', "None", "None")
        flag = data.remove_contact('user', 'sagiv')
        data.delete_database('user')
        self.assertEqual(flag, True)

    def test_update(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user', 'RegularUser')
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
        data.create_var_table('user', 'RegularUser')
        data.create_detection_table('user')
        data.insert_new_contact('user', 'sagiv', 'talker', 'sagiv', "None", "None")
        data.add_detection('user', 1, 1, 2020, 'a')
        data.add_detection('user', 1, 1, 2020, 'a')
        check = data.get_detection_by_day('user', 1, 1, 2020)
        data.delete_database('user')
        x = [(1, 1, 1, 2020, 'a'), (2, 1, 1, 2020, 'a')]
        self.assertEqual(check, x)

    def test_get_user_info(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user', 'RegularUser')
        data.create_detection_table('user')
        x = ("first", 'last', 'id', 'user', 'password')
        check = data.get_user_info('user')
        data.delete_database('user')
        self.assertEqual(check[0], x)

    def test_get_fail(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user', 'RegularUser')
        data.create_detection_table('user')
        data.create_fail_list('user')
        data.add_fail('user', 1, 1, 2020, 'probleam', 'probleam', 'open')
        data.add_fail('user', 1, 1, 2020, 'probleam2', 'probleam2', 'open')
        x = [(1, 1, 1, 2020, 'probleam', 'probleam', 'open'), (2, 1, 1, 2020, 'probleam2', 'probleam2', 'open')]
        check = data.get_fails('user')
        data.delete_database('user')
        self.assertEqual(check, x)

    def test_get_fails_by_day(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user', 'RegularUser')
        data.create_detection_table('user')
        data.create_fail_list('user')
        data.add_fail('user', 1, 1, 2020, 'probleam', 'probleam', 'open')
        x = (1, 1, 1, 2020, 'probleam', 'probleam', 'open')
        check = data.get_fails_by_day('user', 1, 1, 2020)[0]
        data.delete_database('user')
        self.assertEqual(check, x)

    def test_get_detection_by_nick(self):
        data = database.DataBase('user')
        data.create_user_info_table("first", 'last', 'id', 'user', 'password')
        data.create_contact_list_table('user')
        data.create_var_table('user', 'RegularUser')
        data.create_detection_table('user')
        data.create_fail_list('user')
        data.add_detection('user', 1, 1, 2020, 'sagiv')
        data.add_detection('user', 1, 12, 2019, 'marina')
        data.add_detection('user', 3, 5, 2019, 'marina')
        x = [(2, 1, 12, 2019, 'marina'), (3, 3, 5, 2019, 'marina')]
        check = data.get_detection_by_nick('user','marina')
        data.delete_database('user')
        self.assertEqual(check, x)


if __name__ == '__main__':
    unittest.main()
