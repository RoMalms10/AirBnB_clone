#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter Amenity subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
import models
import io
import os
import json
import unittest


class TestAmenity(unittest.TestCase):
    """A TestAmenity class with test functions for the Amenity subclass"""
    def setUp(self):
        self.a = Amenity()

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_is_amenity_instance_base_model(self):
        """Test instantiation of an Amenity class"""
        self.assertTrue(self.a, BaseModel)

    def test_amenity_id_created(self):
        """ """
        self.assertTrue(hasattr(self.a, "id"))

    def test_amenity_created_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "created_at"))

    def test_amenity_updated_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "updated_at"))

    def test_amenity_name(self):
        """ """
        self.assertEqual(self.a.name, "")
