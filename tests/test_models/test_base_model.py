#!/usr/bin/python3
"""Unittest for BaseModel class"""

import json
import os
from uuid import uuid4
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine import file_storage


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """
        Set up for the tests.
        """

        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        self.storage = file_storage.FileStorage()
        self.instance = BaseModel()

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("file.json")
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_init(self):
        """Test BaseModel class initialization"""
        self.assertIs(type(self.instance), BaseModel)
        self.assertIsInstance(self.instance, BaseModel)
        self.assertIsInstance(self.instance, BaseModel)

    def test_init_kwargs(self):
        """Test BaseModel class initialization with **kwargs"""
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)
        self.assertIsInstance(self.instance.id, str)

    def test_instance_creation(self):
        """Test BaseModel self.instance creation"""
        self.assertIsInstance(self.instance, BaseModel)

    def test_unique_id(self):
        """Test BaseModel self.instance has unique id"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at_attribute(self):
        """Test BaseModel self.instance has created_at
        attribute set to current datetime"""
        self.assertIsInstance(self.instance.created_at, datetime)
        # self.assertEqual(self.instance.created_at, instance.updated_at)

    def test_updated_at_attribute(self):
        """Test BaseModel self.instance has updated_at
        attribute set to current datetime"""
        self.assertIsInstance(self.instance.updated_at, datetime)
        # self.assertEqual(self.instance.created_at, instance.updated_at)

    def test_string_representation(self):
        """Test BaseModel self.instance can be printed as string"""
        # fmt: off
        expected_output = (
            f"[{self.instance.__class__.__name__}] ({self.instance.id}) "
            + f"{self.instance.__dict__}"
        )
        # fmt: on
        self.assertEqual(str(self.instance), expected_output)

    def test_save_method(self):
        """Test BaseModel instance can be saved successfully"""
        from models.base_model import BaseModel

        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_multiple_saves(self):
        """Test BaseModel instance can be saved multiple times
        with updated updated_at attribute"""
        from models.base_model import BaseModel

        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        instance.save()
        self.assertNotEqual(new_updated_at, instance.updated_at)

    def test_id_attribute_type(self):
        """Test BaseModel instance has id attribute of type string"""
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)

    def test_created_at_attribute_type(self):
        """Test BaseModel instance has created_at attribute of type datetime"""
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_attribute_type(self):
        """Test BaseModel instance has updated_at attribute of type datetime"""
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_instantiation_with_dict(self):
        """Test BaseModel instance can be instantiated from dictionary"""
        # Define a dictionary with the required keys
        data = {
            "id": str(uuid4()),
            "updated_at": datetime.now().isoformat(),
            "created_at": datetime.now().isoformat(),
        }

        # Pass the dictionary to the BaseModel constructor
        bm = BaseModel(**data)

        # Check that the object has the correct attributes
        self.assertEqual(bm.id, data["id"])
        self.assertEqual(bm.updated_at.isoformat(), data["updated_at"])
        self.assertEqual(bm.created_at.isoformat(), data["created_at"])


class TestBaseModelSave(unittest.TestCase):
    def setUp(self):
        """Sets up test methods"""
        try:
            os.remove("test.json")
        except IOError:
            pass

    def tearDown(self):
        """Tears down test methods"""
        self.setUp()
        # try:
        #     os.remove("test.json")
        # except IOError:
        #     pass

    def test_save(self):
        """
        Test that save properly serializes __objects to the JSON file
        """
        # You might need to read the file and check its contents
        try:
            with open("test.json") as f:
                obj = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return
        instance = BaseModel()
        instance.save()
        with open("test.json") as f:
            obj2 = json.load(f)
        self.assertEqual(obj, obj2)

    def test_reload(self):
        try:
            with open("test.json") as f:
                obj = json.load(f)
        except IOError:
            return
        from models import storage
        from models.base_model import BaseModel

        instance = BaseModel()

        self.assertEqual(obj, storage.all())


class TestToDict(unittest.TestCase):
    #  BaseModel instance can be converted to dictionary with all attributes
    def test_to_dict_all_attributes(self):
        """Test the to_dict method"""
        instance = BaseModel()
        expected_dict = {
            "updated_at": instance.updated_at.isoformat(),
            "id": instance.id,
            "created_at": instance.created_at.isoformat(),
        }
        self.assertEqual(instance.to_dict()["id"], expected_dict["id"])

    def test_to_dict(self):
        """Test the to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertIsInstance(model_dict["created_at"], str)

    def test_to_dict_class_attribute(self):
        """Test the to_dict method"""
        instance = BaseModel()
        expected_dict = {
            "__class__": instance.__class__.__name__,
            "updated_at": instance.updated_at.isoformat(),
            "id": instance.id,
            "created_at": instance.created_at.isoformat(),
        }
        self.assertEqual(instance.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
