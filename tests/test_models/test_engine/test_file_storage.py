#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter FileStorage class
"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import io
import models
import os
import sys
import unittest


class TestFileStorage(unittest.TestCase):
    """A TestFileStorage class with test functions for the FileStorage class"""

    def setUp(self):
        """ Sets up testing environment so previous file storage
            is not affected
        """
        self.file_path = models.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, 'test_storage')

    def tearDown(self):
        """ Removes JSON file after test cases run """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists('test_storage'):
            os.rename('test_storage', self.file_path)

    def test_saves_new_instance(self):
        """ Tests if file is being created """
        a = BaseModel()
        models.storage.new(a)
        models.storage.save()
        file_exist = os.path.exists(self.file_path)
        self.assertTrue(file_exist)

    def test_saves_attributes(self):
        """Tests if attributes are being saved right"""
        a = BaseModel()
        a.my_number = 8
        models.storage.new(a)
        models.storage.save()
        self.assertEqual(a.my_number, 8)

    def test_saves_correct_key(self):
        """Tests if the key is being created correctly"""
        a = BaseModel()
        models.storage.save()
        expected_key = "{}.{}".format("BaseModel", a.id)
        with open(self.file_path, "r", encoding="UTF-8") as f:
            self.assertTrue(expected_key in f.read())

    def test_saves_to_a_file(self):
        """Tests if saving to a file and populates the file"""
        a = BaseModel()
        models.storage.new(a)
        models.storage.save()
        self.assertTrue(os.stat(self.file_path).st_size != 0)

    def test_saves_to_correct_file(self):
        """Test that reload() reloads the JSON from file"""
        self.assertEqual(models.storage._FileStorage__file_path, "file.json")

    def test_storage_objects_dict(self):
        """ Tests if __objects is a dict """
        self.assertEqual(type(models.storage._FileStorage__objects), dict)

    def test_saves_all_method(self):
        """ Tests if the all method works """
        a = BaseModel()
        models.storage.new(a)
        models.storage.save()
        saved_dict = models.storage.all()
        self.assertEqual(saved_dict, models.storage._FileStorage__objects)

    def test_saves_new_method(self):
        """ Tests the new method """
        a = BaseModel()
        models.storage.new(a)
        models.storage.save()
        expected_key = "{}.{}".format("BaseModel", a.id)
        for key in models.storage.all():
            if key == expected_key:
                self.assertEqual(key, expected_key)
