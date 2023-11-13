#!/usr/bin/python3

"""Unittest for file_storage.py"""

import unittest
from models.engine import file_storage
import json


class TestFileStorage(unittest.TestCase):
    def test_file_storage(self):
        """
        Test the file storage class
        """
        store = file_storage.FileStorage()
        self.assertIsInstance(store, file_storage.FileStorage)
        # self.assertEqual(store.__file_path, "file.json")
        # self.assertIsInstance(store.__objects, dict)
        # self.assertEqual(store.__objects, {})
        self.assertTrue(hasattr(store, "all"))
        self.assertTrue(hasattr(store, "new"))
        self.assertTrue(hasattr(store, "save"))
        self.assertTrue(hasattr(store, "reload"))

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
        store.save()
        with open("test.json") as f:
            obj2 = json.load(f)
        self.assertEqual(obj, obj2)

        try:
            with open("test.json") as f:
                obj = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return
        store.reload()
        self.assertEqual(obj, store.all())


if __name__ == "__main__":
    unittest.main()
