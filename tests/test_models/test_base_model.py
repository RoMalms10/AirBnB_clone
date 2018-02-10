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
        self.assertIsNotNone(a.created_at)

    def test_save(self):
        """Test that save() saves datetime"""
        a = BaseModel()
        self.assertIsNotNone(a.updated_at)

        """def test__str__(self):
        Test that a string representation is returned
        a = BaseModel()
        capturedOutput = io.StringIO()
        print(a)
        sys.stdout = capturedOutput
        expected = [a.__class__.name] (<a.id>) <self.__dict__>
        self.assertEqual(capturedOutput.getvalue(), expected)"""

    def test_to_dict(self):
        """Test that to_dict() returns a dictionary containing all
        keys/values of __dict__ of an instance"""
        a = BaseModel()
        self.assertIsNotNone(a.to_dict())
        self.assertIsInstance(a.to_dict(), dict)

    def test_model_from_dict(self):
        """Test of recreation of an instance with a dict representation"""
        test_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                     'created_at': '2017-09-28T21:03:54.052298',
                     'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302',
                     'name': 'Holberton'}
        my_new_model = BaseModel(**test_dict)
        self.assertEqual(my_new_model.id, test_dict.get('id'))
