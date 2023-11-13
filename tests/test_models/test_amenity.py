#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
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
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("file.json")
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_amenity(self):
        """Test the Amenity class"""
        self.assertEqual(self.amenity.name, "")

        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))

        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.name, str)

        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_str(self):
        """Test for __str__ method"""
        self.amenity = Amenity()
        self.assertEqual(
            str(self.amenity),
            "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__),
        )

    def test_to_dict(self):
        """Test for to_dict method"""
        self.amenity = Amenity()
        self.assertEqual(type(self.amenity.to_dict()), dict)
        self.assertTrue(self.amenity.to_dict()["__class__"], "Amenity")
        self.assertTrue("to_dict" in dir(self.amenity))
