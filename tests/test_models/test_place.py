#!/usr/bin/python3
"""
Unittest for Airbnb clone command interpreter Place subclass
"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place
import models
import io
import os
import json
import unittest


class TestPlace(unittest.TestCase):
    """A TestPlace class with test functions for the Place subclass"""
    def setUp(self):
        self.a = Place()

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_is_place_instance_base_model(self):
        """Test instantiation of a Place subclass"""
        self.assertTrue(self.a, BaseModel)

    def test_place_id_created(self):
        """ """
        self.assertTrue(hasattr(self.a, "id"))

    def test_place_created_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "created_at"))

    def test_place_updated_at(self):
        """ """
        self.assertTrue(hasattr(self.a, "updated_at"))

    def test_place_city_id(self):
        """ """
        self.assertEqual(self.a.city_id, "")

    def test_place_user_id(self):
        """ """
        self.assertEqual(self.a.user_id, "")

    def test_place_name(self):
        """ """
        self.assertEqual(self.a.name, "")

    def test_place_description(self):
        """ """
        self.assertEqual(self.a.description, "")

    def test_place_number_rooms(self):
        """ """
        self.assertEqual(self.a.number_rooms, 0)

    def test_place_number_bathrooms(self):
        """ """
        self.assertEqual(self.a.number_bathrooms, 0)

    def test_place_max_guest(self):
        """ """
        self.assertEqual(self.a.max_guest, 0)

    def test_place_price_by_night(self):
        """ """
        self.assertEqual(self.a.price_by_night, 0)

    def test_place_latitude(self):
        """ """
        self.assertEqual(self.a.latitude, 0.0)

    def test_place_longitude(self):
        """ """
        self.assertEqual(self.a.longitude, 0.0)

    def test_place_amenity_ids(self):
        """ """
        self.assertEqual(self.a.amenity_ids, "")
