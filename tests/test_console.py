#!/usr/bin/python3
"""Unittest for console.py"""
import pep8
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    from models.base_model import BaseModel
    from models.engine.file_storage import FileStorage
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("quit")
            self.assertEqual(fake_out.getvalue(), "")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            self.assertIn("b", fake_out.getvalue())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel")
            self.assertEqual(fake_out.getvalue(), "** class doesn't exist **\n")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(fake_out.getvalue(), "** class doesn't exist **\n")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            self.assertEqual(fake_out.getvalue(), "[]\n")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update BaseModel")
            self.assertEqual(fake_out.getvalue(), "** class doesn't exist **\n")
    
    def test_pep8_console(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings(self):
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

if __name__ == '__main__':
    unittest.main()
