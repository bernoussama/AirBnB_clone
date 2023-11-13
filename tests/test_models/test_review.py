#!/usr/bin/python3

import os
import unittest
from models.base_model import BaseModel
from models.review import Review

from models.engine import file_storage


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

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

        self.review = Review()

    def tearDown(self):
        """Tears down test methods"""
        try:
            os.remove("file.json")
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_review(self):
        """Test for Review class"""
        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
        self.assertIsInstance(self.review.id, str)
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(issubclass(Review, BaseModel))

    def test_str(self):
        """Test for __str__ method"""
        self.assertEqual(
            str(self.review),
            "[Review] ({}) {}".format(self.review.id, self.review.__dict__),
        )

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertEqual(type(self.review.to_dict()), dict)
        self.assertTrue(self.review.to_dict()["__class__"], "Review")
        self.assertTrue("to_dict" in dir(self.review))
