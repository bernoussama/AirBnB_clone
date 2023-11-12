#!/usr/bin/python3

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class"""

    def test_user(self):
        """Test the User class"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Holberton"
        my_user.email = ""
        my_user.password = "root"
        self.assertEqual(my_user.first_name, "Betty")
        self.assertEqual(my_user.last_name, "Holberton")
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "root")


if __name__ == "__main__":
    unittest.main()
