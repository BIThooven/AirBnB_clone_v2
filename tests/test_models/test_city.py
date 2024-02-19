#!/usr/bin/python3
"""test for city"""
import unittest
from models.city import City
from models.base_model import BaseModel
import os


class TestCity(unittest.TestCase):
    """this will test the city class"""

    @classmethod
    def setUpClass(cls):
        cls.city = City()
        cls.city.name = "Los Angles"
        cls.city.state_id = "California"

    @classmethod
    def teardown(cls):
        del cls.city

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_checking_for_docstring_city(self):
        self.assertIsNotNone(City.__doc__)

    def test_attributes_city(self):
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_city(self):
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_city(self):
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'Not file engine')
    def test_save_city(self):
        """test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_city(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
