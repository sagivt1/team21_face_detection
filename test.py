import unittest
import database
import RegularUser
import Tester
import Manager
import Sound
import Person


class Test(unittest.TestCase):

    def test_my_contacts_regular_user(self):
        x = RegularUser.RegularUser('sagiv', 'talker', '1', 'sagiv', '123456')
        x.create_database()
        x.data.insert_new_contact('sagiv', 'sagiv', 'talker', 'sagiv', 'path', 'path')
        x.data.insert_new_contact('sagiv', 'marina', 'hatam', 'marina', 'path', 'path')
        ans = x.data.get_all_contacts('sagiv')
        x.delete_my_account()
        check = [('marina', 'marina', 'hatam', 'path', 'path'), ('sagiv', 'sagiv', 'talker', 'path', 'path')]
        self.assertEqual(ans, check)

    def test_add_contact_regular_user(self):
        x = RegularUser.RegularUser('or', 'machluf', '1', 'or', '123456')
        x.create_database()
        x.data.insert_new_contact('or', 'sagiv', 'talker', 'sagiv', 'path', 'path')
        ans = x.data.get_contact('or', 'sagiv')
        check = ('sagiv', 'sagiv', 'talker', 'path', 'path')
        x.delete_my_account()
        self.assertEqual(ans, check)

    def test_my_contacts_tester(self):
        x = Tester.Tester('sagiv', 'talker', '1', 'sagiv', '123456')
        x.create_database()
        x.data.insert_new_contact('sagiv', 'sagiv', 'talker', 'sagiv', 'path', 'path')
        x.data.insert_new_contact('sagiv', 'marina', 'hatam', 'marina', 'path', 'path')
        ans = x.data.get_all_contacts('sagiv')
        x.delete_my_account()
        check = [('marina', 'marina', 'hatam', 'path', 'path'), ('sagiv', 'sagiv', 'talker', 'path', 'path')]
        self.assertEqual(ans, check)

    def test_add_contact_tester(self):
        x = Tester.Tester('or', 'machluf', '1', 'or', '123456')
        x.create_database()
        x.data.insert_new_contact('or', 'sagiv', 'talker', 'sagiv', 'path', 'path')
        ans = x.data.get_contact('or', 'sagiv')
        check = ('sagiv', 'sagiv', 'talker', 'path', 'path')
        x.delete_my_account()
        self.assertEqual(ans, check)

    def test_add_fail(self):
        x = Tester.Tester('mali', 'baratal', '1', 'mali', '123456')
        x.create_database()
        x.data.add_fail('mali', 1, 1, 2020, 'problem', 'problem', 'open')
        x.data.add_fail('mali', 24, 12, 2019, 'problem2', 'problem2', 'open')
        ans = x.data.get_fails('mali')
        check = [(1, 1, 1, 2020, 'problem', 'problem', 'open'), (2, 24, 12, 2019, 'problem2', 'problem2', 'open')]
        x.delete_my_account()
        self.assertEqual(ans, check)

    def test_contact_not_found(self):
        x = RegularUser.RegularUser('marina', 'hatam', '1', 'marina', '123456')
        x.create_database()
        x.data.insert_new_contact('marina', 'sagiv', 'talker', 'sagiv', 'path', 'path')
        check = ('marina', 'marina', 'hatam', 'path', 'path')
        ans = x.data.get_contact('marina', 'sagiv')
        x.delete_my_account()
        self.assertNotEqual(ans, check)

    def test_edit_channge_details(self):
        x = RegularUser.RegularUser('marina', 'hatam', '1', 'marina', '123456')
        x.create_database()
        y = Tester.Tester('mali', 'baratal', '1', 'mali', '123456')
        y.create_database()
        x.data.update_user_name('marina', 'aaa')
        y.data.update_user_name('mali', 'bbb')
        x.data.update_last_name('marina', 'aaa')
        y.data.update_last_name('mali', 'bbb')
        x.data.update_password('marina', '123')
        y.data.update_password('mali', '123')
        ans = x.data.get_user_info('marina')
        ans.append(y.data.get_user_info('mali')[0])
        x.delete_my_account()
        y.delete_my_account()
        check = [('marina', 'aaa', '1', 'aaa', '123'), ('mali', 'bbb', '1', 'bbb', '123')]
        self.assertEqual(ans, check)

    def test_update_fail_status(self):
        y = Tester.Tester('or', 'machluf', '1', 'or', '123456')
        y.create_database()
        y.data.add_fail('or', 1, 1, 2020, 'problem', 'problem', 'open')
        y.data.update_status('or', 1, 'close')
        ans = y.data.get_fails_by_day('or', 1, 1, 2020)
        y.delete_my_account()
        check = (1, 1, 1, 2020, 'problem', 'problem', 'close')
        self.assertEqual(ans[0], check)


if __name__ == '__main__':
    unittest.main()
