#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter City subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
import io
import os
import sys
import unittest


class TestCity(unittest.TestCase):
    """A TestCity class with test functions for the City subclass"""

    def test_instantiation(self):
        """Test instantiation of a City subclass"""
        a = City()
        self.assertTrue(a, BaseModel)
