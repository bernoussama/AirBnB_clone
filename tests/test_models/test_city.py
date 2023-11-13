#!/usr/bin/python3

import os
import unittest
from models.base_model import BaseModel
from models.city import City

from models.engine import file_storage


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        """
        Set up for the tests.
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        self.storage = file_storage.FileStorage()
        self.storage.__file_path = "test.json"

        self.city = City()

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("file.json")
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_city(self):
        """Test for City class"""
        self.assertIsInstance(self.city, City)
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        self.assertIsInstance(self.city.id, str)
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(issubclass(City, BaseModel))

    def test_str(self):
        """Test for __str__ method"""
        self.assertEqual(
            str(self.city),
            "[City] ({}) {}".format(self.city.id, self.city.__dict__),
        )

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertEqual(type(self.city.to_dict()), dict)
        self.assertTrue(self.city.to_dict()["__class__"], "City")
        self.assertTrue("to_dict" in dir(self.city))
