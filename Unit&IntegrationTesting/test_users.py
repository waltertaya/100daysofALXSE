import unittest
from users import User


class TestUser(unittest.TestCase):

    # setUp and teardown class methods run before and after running class
    @classmethod
    def setUpClass(cls):
        cls.user1 = User(2348, 'taya', 'walter@gmail.com')
        cls.user2 = User(4529, 'regy', 'reginah@gmail.com')
        cls.user3 = User(4529, 'brett', 'brettcooper@gmail.com')

    @classmethod
    def tearDownClass(cls):
        pass

    # Setup and teardown methods run before and after every method
    def setUp(self):
        self.user1.login()
        self.user2.login()
        self.user3.login()

    def tearDown(self):
        self.user1.logout()
        self.user2.logout()
        self.user3.logout()

    def test_login(self):
        self.assertTrue(self.user1.logged_in)
        self.assertTrue(self.user2.logged_in)
        self.assertTrue(self.user3.logged_in)
    
    def test_logout(self):
        self.user1.logout()
        self.assertFalse(self.user1.logged_in)
    
    def test_update_email(self):
        self.user3.update_email('cooper@gmail.com')
        self.assertEqual(self.user3.email, 'cooper@gmail.com')

    def test_update_email_invalid(self):
        with self.assertRaises(ValueError):
            self.user3.update_email('invalid-email')


if __name__ == '__main__':
    unittest.main()
