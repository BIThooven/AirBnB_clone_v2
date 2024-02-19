#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8
import unittest


class test_Amenity(unittest.TestCase):
    from models.base_model import BaseModel
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
    
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_pep8_Amenity(self):
        """ """
        p = pep8.StyleGuide(quiet=True)
        r = p.check_files(['models/amenity.py'])
        self.assertEqual(r.total_errors, 0, "pep8 error")

    def test_module_docstring(self):
        """ """
        self.assertTrue(len(Amenity.__doc__) > 1)

    def test_class_docstring(self):
        """ """
        self.assertTrue(len(Amenity.__doc__) > 1)

    def test_method_docstring(self):
        """ """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 1)

    def test_instance(self):
        """ """
        obj = self.value()
        self.assertIsInstance(obj, self.value)

    def test_is_subclass(self):
        """ """
        obj = self.value()
        self.assertTrue(issubclass(obj.__class__, BaseModel), True)

    def test_save_amenity(self):
        """ """
        obj = self.value()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_to_dict_amenity(self):
        """ """
        obj = self.value()
        new_dict = obj.to_dict()
        self.assertEqual(obj.__class__.__name__, 'Amenity')
        self.assertIsInstance(new_dict['created_at'], str)
        self.assertIsInstance(new_dict['updated_at'], str)

    def test_hasattribute(self):
        """ """
        obj = self.value()
        self.assertTrue(hasattr(obj, "name"))

if __name__ == '__main__':
    unittest.main()
