#!/usr/bin/python3
""" test for base_model """
import unittest
from models.base_model import BaseModel
import os
import pep8
import datetime


class TestBaseModel(unittest.TestCase):
    """testing BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """ """
        cls.base = BaseModel()
        cls.base.name = "Holberton"

    @classmethod
    def teardown(cls):
        """ """
        del cls.base

    def tearDown(self):
        """ """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_checking_for_docstring_BaseModel(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def test_attributes_BaseModel(self):
        self.assertTrue('id' in self.base.__dict__)
        self.assertTrue('created_at' in self.base.__dict__)
        self.assertTrue('updated_at' in self.base.__dict__)

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.base.__class__, BaseModel), True)

    def test_attribute_types(self):
        self.assertEqual(type(self.base.id), str)
        self.assertEqual(type(self.base.created_at), datetime.datetime)
        self.assertEqual(type(self.base.updated_at), datetime.datetime)

    def test_save(self):
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.base), True)
        self.assertIsInstance(self.base.to_dict()['updated_at'], str)
        self.assertIsInstance(self.base.to_dict()['created_at'], str)

    def test_str(self):
        self.assertEqual(str(self.base), "[BaseModel] ({}) {}".format(
            self.base.id, self.base.__dict__))
        
if __name__ == "__main__":
    unittest.main()
