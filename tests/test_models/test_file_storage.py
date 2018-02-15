#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter FileStorage class
"""
from datetime import datetime
from models.engine.file_storage import FileStorage
import io
import os
import sys
import unittest


class TestFileStorage(unittest.TestCase):
    """A TestFileStorage class with test functions for the FileStorage class"""

    def test_instantiation(self):
        """Test instantiation of a FileStorage class"""
        a = FileStorage()
        self.assertIs(type(a), FileStorage)

    def test_reload(self):
        """Test that reload() reloads the JSON from file"""
        test_object = {'__class__': 'FileStorage', 'id': 89, 'name': 'test'}
        FileStorage.new(self, test_object)
        FileStorage.save()
        self.assertEqual(FileStorage.all(), test_object)
