#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import datetime
from models.engine import file_storage
import os


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

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

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("file.json")
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_amenity(self):
        """Test the Amenity class"""
        my_amenity = Amenity()
        my_amenity.name = "Betty"
        self.assertEqual(my_amenity.name, "Betty")
        self.assertTrue(hasattr(my_amenity, "id"))
        self.assertTrue(hasattr(my_amenity, "created_at"))
        self.assertTrue(hasattr(my_amenity, "updated_at"))
        self.assertTrue(hasattr(my_amenity, "name"))
        self.assertIsInstance(my_amenity.created_at, datetime.datetime)
        self.assertIsInstance(my_amenity.updated_at, datetime.datetime)
        self.assertIsInstance(my_amenity.id, str)
        self.assertIsInstance(my_amenity.name, str)
        self.assertTrue(issubclass(Amenity, BaseModel))
