import unittest
import database


class TestDataBase(unittest.TestCase):

    def test_insert_and_get(self):
        data = database.DataBase()
        data.insert_new_contact('sagiv', 'talker', 'sagiv')
        x = ("sagiv", "sagiv", "talker")
        check = data.get_contact("sagiv")
        data.delete_database()
        self.assertEqual(check, x)

    def test_get_all_contact(self):
        data = database.DataBase()
        data.insert_new_contact('sagiv', 'talker', 'sagiv')
        data.insert_new_contact("or","machlouf","or")
        x = [("or","or","machlouf"),("sagiv", "sagiv", "talker")]
        check = data.get_all_contacts()
        data.delete_database()
        self.assertEqual(check, x)

    def test_remove_contact(self):
        data = database.DataBase()
        data.insert_new_contact('sagiv', 'talker', 'sagiv')
        flag = data.remove_contact('sagiv')
        data.delete_database()
        self.assertEqual(flag, True)

    def test_update(self):
        data = database.DataBase()
        data.insert_new_contact('sagiv', 'talker', 'sagiv')
        data.update_last_name('sagiv', 'c')
        data.update_first_name('sagiv', 'b')
        data.update_nick_name('sagiv', 'a')
        x = ('a', 'b', 'c')
        check = data.get_contact('a')
        data.delete_database()
        self.assertEqual(check,x)




if __name__ == '__main__':
    unittest.main()
