#!/usr/bin/python3

from datetime import datetime
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

        self.assertTrue(hasattr(my_user, "id"))
        self.assertTrue(hasattr(my_user, "created_at"))
        self.assertTrue(hasattr(my_user, "updated_at"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))

        self.assertIsInstance(my_user.created_at, datetime)
        self.assertIsInstance(my_user.updated_at, datetime)
        self.assertIsInstance(my_user.id, str)
        self.assertIsInstance(my_user.first_name, str)
        self.assertIsInstance(my_user.last_name, str)
        self.assertIsInstance(my_user.email, str)
        self.assertIsInstance(my_user.password, str)

    def test_first_name(self):
        """Test the User class"""
        my_user = User()
        my_user.first_name = "Betty"
        self.assertEqual(my_user.first_name, "Betty")

    def test_last_name(self):
        """Test the User class"""
        my_user = User()
        my_user.last_name = "Holberton"
        self.assertEqual(my_user.last_name, "Holberton")

    def test_email(self):
        """Test the User class"""
        my_user = User()
        my_user.email = "email@alx.com"
        self.assertEqual(my_user.email, "email@alx.com")

    def test_password(self):
        """Test the User class"""
        my_user = User()
        my_user.password = "root"
        self.assertEqual(my_user.password, "root")


if __name__ == "__main__":
    unittest.main()
