#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter City subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City
import models
import io
import os
import json
import unittest


class TestCity(unittest.TestCase):
    """A TestCity class with test functions for the City subclass"""
    def setUp(self):
        self.a = City()

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_is_city_instance_base_model(self):
        """Test instantiation of a City subclass"""
        self.assertTrue(self.a, BaseModel)

    def test_city_id_created(self):
        """ """
        self.assertTrue(hasattr(self.a, "id"))

    def test_city_created_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "created_at"))

    def test_city_updated_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "updated_at"))

    def test_city_name(self):
        """ """
        self.assertEqual(self.a.name, "")

    def test_city_state_id(self):
        """ """
        self.assertEqual(self.a.state_id, "")
