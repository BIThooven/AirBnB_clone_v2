#!/usr/bin/python3
""" testing review"""
from models.base_model import BaseModel
from models.review import Review
import unittest
import os

class TestReview(unittest.TestCase):
    """testing Place class"""
    def setUp(self):
        """set up for testing"""
        self.review = Review()
        self.review.place_id = "123"
        self.review.user_id = "123"
        self.review.text = "text"

    def tearDown(self):
        """at the end of the test this will tear it down"""
        del self.review

    def test_docstring(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attribute_types(self):
        """testing the attributes"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_is_subclass(self):
        """test if Review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Testing database storage only")
    def test_save(self):
        """test if the save works"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
