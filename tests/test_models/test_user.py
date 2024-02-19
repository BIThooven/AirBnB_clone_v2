#!/usr/bin/python3
""" """
from unittest import TestCase, skipIf, main
import os
from models.base_model import BaseModel
from models.user import User


class test_user(TestCase):
    """ """
    def setUp(self):
        """ """
        self.user = User()
        self.user.first_name = "Guillaume"
        self.user.last_name = "Snow"
        self.user.email = "gui@hbtn.io"
        self.user.password = "guipwd"

    def tearDown(self):
        """ """
        del self.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_doc(self):
        """ """
        self.assertIsNotNone(User.__doc__)

    def test_attr(self):
        """ """
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertEqual('first_name' in self.user.__dict__, True)
        self.assertEqual('created_at' in self.user.__dict__, True)
        self.assertEqual('email' in self.user.__dict__, True)

    def test_type(self):
        """ """
        self.assertTrue(type(self.user.first_name) is str)
        self.assertTrue(type(self.user.last_name) is str)
        self.assertTrue(type(self.user.email) is str)
        self.assertTrue(type(self.user.password) is str)

    def test_instance(self):
        """ """
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    @skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_save(self):
        """ """
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """ """
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

    def test_str(self):
        """ """
        self.assertEqual(str(self.user), "[User] ({}) {}".format(
            self.user.id, self.user.__dict__))
        
if __name__ == "__main__":
    main()
