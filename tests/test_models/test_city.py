#!/usr/bin/python3
"""Unittest for City"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_city_inherits_from_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_has_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'places'))

    def test_city_attributes_are_strings(self):
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_places_relationship(self):
        city = City()
        self.assertTrue(hasattr(city, 'places'))
        self.assertIsInstance(city.places, list)


if __name__ == '__main__':
    unittest.main()
