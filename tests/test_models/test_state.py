#!/usr/bin/python3
""" """
from unittest import TestCase, skipIf, main
import os
from models.state import State
from models.base_model import BaseModel

class test_state(TestCase):
    """ """
    def setUp(self):
        """ """
        self.state = State()
        self.state.name = "California"

    def tearDown(self):
        """ """
        del self.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_doc(self):
        """ """
        self.assertIsNotNone(State.__doc__)

    def test_attr(self):
        """ """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "California")
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)

    def test_type(self):
        """ """
        self.assertTrue(type(self.state.name) is str)

    def test_instance(self):
        """ """
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    @skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_save(self):
        """ """
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """ """
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_str(self):
        """ """
        self.assertEqual(str(self.state), "[State] ({}) {}".format(
            self.state.id, self.state.__dict__))


if __name__ == "__main__":
    main()
