#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter Place subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
import io
import os
import sys
import unittest


class TestPlace(unittest.TestCase):
    """A TestPlace class with test functions for the Place subclass"""

    def test_place_is_base_subclass(self):
        """Test instantiation of a Place subclass"""
        a = Place()
        self.assertTrue(a, BaseModel)
