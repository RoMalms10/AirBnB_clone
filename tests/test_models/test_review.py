#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter Review subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review
import models
import io
import os
import json
import unittest


class TestReview(unittest.TestCase):
    """A TestReview class with test functions for the Review subclass"""
    def setUp(self):
        self.a = Review()

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_is_review_instance_base_model(self):
        """Test instantiation of a Review subclass"""
        self.assertTrue(self.a, BaseModel)

    def test_review_id_created(self):
        """ """
        self.assertTrue(hasattr(self.a, "id"))

    def test_review_created_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "created_at"))

    def test_review_updated_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "updated_at"))

    def test_review_place_id(self):
        """ """
        self.assertEqual(self.a.place_id, "")

    def test_review_user_id(self):
        """ """
        self.assertEqual(self.a.user_id, "")

    def test_review_text(self):
        """ """
        self.assertEqual(self.a.text, "")
