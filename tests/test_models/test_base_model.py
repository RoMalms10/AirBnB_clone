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
        self.assertEqual(36, len(a.id))

    def test_unique_id(self):
        """ Test if id's are unique """
        a = BaseModel()
        b = BaseModel()
        self.assertIsNot(a, b)

    def test_created_at(self):
        """Test that datetime is assigned when new instance of BaseModel
        is created"""
        a = BaseModel()
        self.assertTrue(hasattr(a, "created_at"))
        self.assertEqual(type(a.created_at), datetime)

    def test_save(self):
        """Test that save() saves datetime"""
        a = BaseModel()
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertEqual(type(a.updated_at), datetime)

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
        self.assertTrue(type(a.created_at), str)
        self.assertTrue(type(a.updated_at), str)
        self.assertEqual(type(a.to_dict()), dict)
        self.assertNotEqual(a.to_dict().get('id'), None)
        self.assertNotEqual(a.to_dict().get('created_at'), None)
        self.assertNotEqual(a.to_dict().get('updated_at'), None)
        self.assertEqual(a.to_dict().get('__class__'), 'BaseModel')

    def test_from_kwargs(self):
        """Test of recreation of an instance with kwargs"""
        test_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                     'created_at': '2017-09-28T21:05:54.119427',
                     'my_number': 89,
                     '__class__': 'BaseModel',
                     'updated_at': '2017-09-28T21:05:54.119572',
                     'name': 'Holberton'}
        my_new_model = BaseModel(**test_dict)
        self.assertEqual(my_new_model.id, test_dict.get('id'))
        self.assertEqual(my_new_model.name, test_dict.get('name'))
        self.assertEqual(my_new_model.created_at.isoformat(),
                         test_dict.get('created_at'))
        self.assertEqual(my_new_model.updated_at.isoformat(),
                         test_dict.get('updated_at'))
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
