#!/usr/bin/python3
"""test for amenity"""
import unittest
from os import remove
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """this will test the Amenity class"""

    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()
        cls.amenity.name = "WiFi"

    @classmethod
    def teardown(cls):
        del cls.amenity

    def tearDown(self):
        try:
            remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_amenity(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_amenity(self):
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types(self):
        self.assertEqual(type(self.amenity.name), str)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
