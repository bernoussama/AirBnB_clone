#!/usr/bin/python3

import unittest


class TestModels(unittest.TestCase):
    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1, bm2)
        self.assertIsInstance(bm1.id, str)
