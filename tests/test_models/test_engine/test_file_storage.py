#!/usr/bin/python3

"""Unittest for file_storage.py"""

import unittest
from models.engine import file_storage
from models.base_model import BaseModel
from models import storage
import json


class TestFileStorage(unittest.TestCase):
    def test_file_storage(self):
        """
        Test the file storage class
        """
        store = file_storage.FileStorage()
        self.assertIsInstance(store, file_storage.FileStorage)
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertEqual(storage._FileStorage__file_path, "file.json")
        self.assertTrue(hasattr(store, "all"))
        self.assertTrue(hasattr(store, "new"))
        self.assertTrue(hasattr(store, "save"))
        self.assertTrue(hasattr(store, "reload"))

        self.assertIsInstance(storage.all(), dict)
        self.assertNotEqual(storage.all(), {})

        try:
            with open("test.json") as f:
                obj = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return
        store.new(obj)
        self.assertIn(obj, store.all().values())

        try:
            with open("test.json") as f:
                obj = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return

        storage.save()
        with open("test.json") as f:
            obj2 = json.load(f)
        self.assertEqual(obj, obj2)
        self.assertIn(obj, obj2)
        # self.assertEqual(obj2[f"{obj['__class__']}"], store.to_dict())

        try:
            with open("test.json") as f:
                obj = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return
        store.reload()
        self.assertEqual(obj, store.all())


if __name__ == "__main__":
    unittest.main()
