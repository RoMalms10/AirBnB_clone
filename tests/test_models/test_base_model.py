#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter BaseModel class
"""
from models.base_model import BaseModel
import io
import json
import os
import sys
import unittest


class TestBaseModel(unittest.TestCase):
    """A TestBaseModel class with test functions for the BaseModel class"""

    def test_instantiation(self):
        """Test instantiation of a BaseModel class"""
        a = BaseModel()
        self.assertIsInstance(a, class)

    def test_id_assignment(self):
        """Test assignment of UUID is converted to string"""
        b = BaseModel()
        self.assertEqual(b.id, uuid.uuid4(b))
    
    def test_unique_id(self):
        """Test unique UUID assignment"""
        c = BaseModel()
        d = BaseModel()
        e = BaseModel()
        f = BaseModel()
        g = BaseModel()
        self.assertEqual(c, d, e, f, g)

    def test_datetime(self):
        """Test that datetime is assigned when new instance of BaseModel is created"""
        h = BaseModel()
        self.assertEqual(h.created_at, h.save)

    def test_to_dict(self):
        """Test that to_dict returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        i = BaseModel()
        self.assertIsInstance(h.to_dict, dict)

    def test_to_string(self):
        """Test that a string representation is returned"""
        h = BaseModel()
        self.assertEqual(h.created_at, h.save)

