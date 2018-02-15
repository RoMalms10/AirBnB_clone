#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter Review subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
import io
import os
import sys
import unittest


class TestReview(unittest.TestCase):
    """A TestReview class with test functions for the Review subclass"""

    def test_is_review_base_model(self):
        """Test instantiation of a Review class"""
        a = Review()
        self.assertTrue(a, BaseModel)
