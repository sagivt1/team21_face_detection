import unittest
import database


class TestDataBase(unittest.TestCase):

    def test_connect(self):
        data = database.DataBase('first','last','id','user','password')
        flag = data.connect('user','password')
        data.delete_database('user')
        self.assertEqual(flag,True)


    # def test_insert_and_get(self):
    #     data = database.DataBase("first", 'last', 'id', 'user', 'password')
    #     data.create_contact_list_table('user')
    #     data.insert_new_contact('user','sagiv', 'talker', 'sagiv')
    #     x = ("sagiv", "sagiv", "talker")
    #     check = data.get_contact('user',"sagiv")
    #     data.delete_database('user')
    #     self.assertEqual(check, x)
    #
    # def test_get_all_contact(self):
    #     data = database.DataBase("first", 'last', 'id', 'user', 'password')
    #     data.create_contact_list_table('user')
    #     data.insert_new_contact('user','sagiv', 'talker', 'sagiv')
    #     data.insert_new_contact('user',"or", "machlouf", "or")
    #     x = [("or", "or", "machlouf"), ("sagiv", "sagiv", "talker")]
    #     check = data.get_all_contacts('user')
    #     data.delete_database('user')
    #     self.assertEqual(check, x)
    #
    # def test_remove_contact(self):
    #     data = database.DataBase("first", 'last', 'id', 'user', 'password')
    #     data.create_contact_list_table('user')
    #     data.insert_new_contact('user','sagiv', 'talker', 'sagiv')
    #     flag = data.remove_contact('user','sagiv')
    #     data.delete_database('user')
    #     self.assertEqual(flag, True)
    #
    # def test_update(self):
    #     data = database.DataBase("first", 'last', 'id', 'user', 'password')
    #     data.create_contact_list_table('user')
    #     data.insert_new_contact('user','sagiv', 'talker', 'sagiv')
    #     data.update_last_name('user','sagiv', 'c')
    #     data.update_first_name('user','sagiv', 'b')
    #     data.update_nick_name('user','sagiv', 'a')
    #     x = ('a', 'b', 'c')
    #     check = data.get_contact('user','a')
    #     data.delete_database('user')
    #     self.assertEqual(check, x)


if __name__ == '__main__':
     unittest.main()
