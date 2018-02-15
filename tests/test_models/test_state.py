#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter State subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
import models
import io
import os
import json
import unittest


class TestState(unittest.TestCase):
    """A TestUser class with test functions for the User subclass"""
    def setUp(self):
        self.a = State()

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_is_state_instance_base_model(self):
        """Test instantiation of a State class"""
        self.assertTrue(self.a, BaseModel)

    def test_state_id_created(self):
        """ """
        self.assertTrue(hasattr(self.a, "id"))

    def test_state_created_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "created_at"))

    def test_state_updated_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "updated_at"))

    def test_state_name(self):
        """ """
        self.assertEqual(self.a.name, "")
