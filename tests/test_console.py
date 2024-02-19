#!/usr/bin/python3
"""Unittest for console.py"""
import pep8
from os import getenv, remove
import unittest
from unittest.mock import patch
from io import StringIO
import console
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test the console"""
    def test_pep8_console(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def setUp(self):
        """Set up for the tests."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down for tests."""
        self.console = None

    def tearDown(self):
        """Tear down for tests."""
        if (getenv('HBNB_TYPE_STORAGE') == 'db'):
            try:
                remove('file.json')
            except Exception:
                pass

    def test_docstrings(self):
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_emptyline(self):
        """testing for emptylines"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd('\n'))
            self.assertEqual('', f.getvalue())

if __name__ == '__main__':
    unittest.main()
