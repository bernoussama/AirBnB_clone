#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.place import Place
import datetime
from models.engine import file_storage
import os


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

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
        self.place = Place()

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("file.json")
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_place(self):
        """Test for Place class"""
        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertIsInstance(self.place.id, str)
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(issubclass(Place, BaseModel))

    def test_str(self):
        """Test for __str__ method"""
        self.assertEqual(
            str(self.place),
            "[Place] ({}) {}".format(self.place.id, self.place.__dict__),
        )

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertEqual(type(self.place.to_dict()), dict)
        self.assertTrue(self.place.to_dict()["__class__"], "Place")
        self.assertTrue("to_dict" in dir(self.place))
