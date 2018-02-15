#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter User subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
import models
import io
import os
import json
import unittest


class TestUser(unittest.TestCase):
    """A TestUser class with test functions for the User subclass"""
    def setUp(self):
        self.a = User()

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_is_user_instance_base_model(self):
        """Test instantiation of a User class"""
        self.assertTrue(self.a, BaseModel)

    def test_user_id_created(self):
        """ """
        self.assertTrue(hasattr(self.a, "id"))

    def test_user_created_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "created_at"))

    def test_user_updated_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "updated_at"))

    def test_user_email(self):
        """ """
        self.assertEqual(self.a.email, "")
