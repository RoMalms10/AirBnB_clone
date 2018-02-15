#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter BaseModel class
"""
from datetime import datetime
from models.base_model import BaseModel
import io
import os
import sys
import unittest


class TestBaseModel(unittest.TestCase):
    """A TestBaseModel class with test functions for the BaseModel class"""

    def test_instantiation(self):
        """Test instantiation of a BaseModel class"""
        a = BaseModel()
        self.assertIs(type(a), BaseModel)

    def test_id_assignment(self):
        """Test assignment of UUID is converted to string"""
        a = BaseModel()
        self.assertIsInstance(a.id, str)
    
    def test_created_at(self):
        """Test that datetime is assigned when new instance of BaseModel is created"""
        a = BaseModel()
        self.assertTrue(hasattr(a, "created_at"))

    def test_save(self):
        """Test that save() saves datetime"""
        a = BaseModel()
        self.assertTrue(hasattr(a, "updated_at"))

    def test_updated_at_updates(self):
        """Test that save() updates datetime"""
        a = BaseModel()
        a_time = getattr(a, "updated_at")
        a.save()
        a_updated = getattr(a, "updated_at")
        self.assertNotEqual(a_time, a_updated)

    def test_to_dict(self):
        """Test that to_dict() returns a dictionary containing all
        keys/values of __dict__ of an instance"""
        a = BaseModel()
        self.assertIsNotNone(a.to_dict())
        self.assertIsInstance(a.to_dict(), dict)
        self.assertTrue(type(a.created_at), str)
        self.assertTrue(type(a.updated_at), str)

    def test_model_from_dict(self):
        """Test of recreation of an instance with a dict representation"""
        test_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                     'created_at': '2017-09-28T21:05:54.119427',
                     'my_number': 89, 'updated_at': '2017-09-28T21:05:54.119572',
                     'name': 'Holberton'}
        my_new_model = BaseModel(**test_dict)
        self.assertEqual(my_new_model.id, test_dict.get('id'))
        self.assertEqual(my_new_model.name, test_dict.get('name'))
        self.assertEqual(my_new_model.created_at.isoformat(), test_dict.get('created_at'))
        self.assertEqual(my_new_model.updated_at.isoformat(), test_dict.get('updated_at'))
        self.assertEqual(my_new_model.my_number, test_dict.get('my_number'))

    def test_str_output(self):
        """Test that a string representation is returned"""
        a = BaseModel()
        expected = "[{}] ({}) {}".format(a.__class__.__name__,
                                        a.id, a.__dict__)
        captured = io.StringIO()
        sys.stdout = captured
        print(a, end="")
        self.assertEqual(captured.getvalue(), expected)
