#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os

class TestBaseModel(unittest.TestCase):

    #  BaseModel instance is created successfully
    def test_instance_creation(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    #  BaseModel instance has unique id
    def test_unique_id(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    #  BaseModel instance has created_at attribute set to current datetime
    def test_created_at_attribute(self):
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertEqual(instance.created_at, instance.updated_at)

    #  BaseModel instance has updated_at attribute set to current datetime
    def test_updated_at_attribute(self):
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.created_at, instance.updated_at)

    #  BaseModel instance can be printed as string
    def test_string_representation(self):
        instance = BaseModel()
        expected_output = f"[{instance.__class__.__name__}] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_output)

    #  BaseModel instance can be saved successfully
    def test_save_method(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    #  BaseModel instance has id attribute of type string
    def test_id_attribute_type(self):
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)

    #  BaseModel instance has created_at attribute of type datetime
    def test_created_at_attribute_type(self):
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    #  BaseModel instance has updated_at attribute of type datetime
    def test_updated_at_attribute_type(self):
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    #  BaseModel instance can be saved multiple times with updated updated_at attribute
    def test_multiple_saves(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        instance.save()
        self.assertNotEqual(new_updated_at, instance.updated_at)

    #  BaseModel instance can be converted to dictionary with all attributes
    def test_to_dict_all_attributes(self):
        instance = BaseModel()
        expected_dict = {
            "updated_at": instance.updated_at.isoformat(),
            "id": instance.id,
            "created_at": instance.created_at.isoformat()
        }
        self.assertEqual(instance.to_dict(), expected_dict)

    #  BaseModel instance can be converted to dictionary with __class__ attribute
    def test_to_dict_class_attribute(self):
        instance = BaseModel()
        expected_dict = {
            "__class__": instance.__class__.__name__,
            "updated_at": instance.updated_at.isoformat(),
            "id": instance.id,
            "created_at": instance.created_at.isoformat()
        }
        self.assertEqual(instance.to_dict(), expected_dict)
