#!/usr/bin/python3
""" My module for amenities """
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity that inherits from BaseModel """
    name = ""
