#!/usr/bin/python3

from datetime import datetime
import unittest
from models.user import User
from models.base_model import BaseModel
import os
from models.engine import file_storage


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """
        Set up for the tests.
        """

        try:
            os.remove("test.json")
        except IOError:
            pass
        self.storage = file_storage.FileStorage()
        self.storage.__file_path = "test.json"
        self.my_user = User()

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("test.json")
        except IOError:
            pass

    def test_user(self):
        """Test the User class"""
        self.my_user.first_name = "Betty"
        self.my_user.last_name = "Holberton"
        self.my_user.email = ""
        self.my_user.password = "root"
        self.assertEqual(self.my_user.first_name, "Betty")
        self.assertEqual(self.my_user.last_name, "Holberton")
        self.assertEqual(self.my_user.email, "")
        self.assertEqual(self.my_user.password, "root")

        self.assertTrue(hasattr(self.my_user, "id"))
        self.assertTrue(hasattr(self.my_user, "created_at"))
        self.assertTrue(hasattr(self.my_user, "updated_at"))
        self.assertTrue(hasattr(self.my_user, "first_name"))
        self.assertTrue(hasattr(self.my_user, "last_name"))
        self.assertTrue(hasattr(self.my_user, "email"))
        self.assertTrue(hasattr(self.my_user, "password"))

        self.assertIsInstance(self.my_user.created_at, datetime)
        self.assertIsInstance(self.my_user.updated_at, datetime)
        self.assertIsInstance(self.my_user.id, str)
        self.assertIsInstance(self.my_user.first_name, str)
        self.assertIsInstance(self.my_user.last_name, str)
        self.assertIsInstance(self.my_user.email, str)
        self.assertIsInstance(self.my_user.password, str)
        self.assertTrue(issubclass(User, BaseModel))

    def test_first_name(self):
        """Test the User class"""
        self.my_user = User()
        self.my_user.first_name = "Betty"
        self.assertEqual(self.my_user.first_name, "Betty")

    def test_last_name(self):
        """Test the User class"""
        self.my_user = User()
        self.my_user.last_name = "Holberton"
        self.assertEqual(self.my_user.last_name, "Holberton")

    def test_email(self):
        """Test the User class"""
        self.my_user = User()
        self.my_user.email = "email@alx.com"
        self.assertEqual(self.my_user.email, "email@alx.com")

    def test_password(self):
        """Test the User class"""
        self.my_user = User()
        self.my_user.password = "root"
        self.assertEqual(self.my_user.password, "root")


if __name__ == "__main__":
    unittest.main()
