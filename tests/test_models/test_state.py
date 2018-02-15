#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter State subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
import io
import os
import sys
import unittest


class TestState(unittest.TestCase):
    """A TestState subclass with test functions for the State subclass"""

    def test_if_state_is_base_model(self):
        """Test instantiation of a State subclass as a BaseModel class"""
        a = State()
        self.assertTrue(a, BaseModel)
