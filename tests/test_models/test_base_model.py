#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter BaseModel class
"""
from models.base_model import BaseModel
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
        self.assertIsInstance(self.id, str)
    
    def test_created_at(self):
        """Test that datetime is assigned when new instance of BaseModel is created"""
        a = BaseModel()
        self.assertIsNotNone(self.created_at)

    def test_save(self):
        """Test that save() saves datetime"""
        a = BaseModel()
        self.assertIsNotNone(self.updated_at)

    def test__str__(self):
        """Test that a string representation is returned"""
        a = BaseModel()
        self.assertIsNotNone(self.__str__)
        self.assertIsInstance(self.__str__, str)

    def test_to_dict(self):
        """Test that to_dict() returns a dictionary containing all
        keys/values of __dict__ of an instance"""
        a = BaseModel()
        self.assertIsNotNone(self.to_dict)
        self.assertIsInstance(self.to_dict, dict)
        self.assertIn(self.__class__, self.to_dict)
