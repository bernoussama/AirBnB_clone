#!/usr/bin/python3

import os
import unittest
from models.base_model import BaseModel
from models.state import State
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

        self.state = State()

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("file.json")
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_subclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(hasattr(State, "name"))
        self.assertEqual(self.state.name, "")
        self.assertIsInstance(self.state.name, str)

    def test_str(self):
        """Test str method"""
        self.assertEqual(
            str(self.state),
            "[State] ({}) {}".format(self.state.id, self.state.__dict__),
        )

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertEqual("to_dict" in dir(self.state), True)
        new_dict = self.state.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertFalse("_sa_instance_state" in new_dict)
        self.assertEqual(new_dict["__class__"], "State")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
