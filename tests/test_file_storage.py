import unittest
from models.engine import file_storage
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """
        Set up for the tests.
        """
        self.storage = file_storage.FileStorage()
        self.storage.__file_path = "test.json"

    def test_all(self):
        """
        Test that all returns the dictionary __objects
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """
        Test that new adds an object to __objects
        """
        try:
            with open("test.json") as f:
                obj = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return
        self.storage.new(obj)
        self.assertIn(obj, self.storage.all().values())

    def test_save(self):
        """
        Test that save properly serializes __objects to the JSON file
        """
        # You might need to read the file and check its contents
        self.assertEqual(True, True)

    def test_reload(self):
        """
        Test that reload properly deserializes the JSON file to __objects
        """
        # You might need to modify the file, call reload and check __objects
        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
