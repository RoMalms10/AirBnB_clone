#!/usr/bin/env python3
""" My module for City """
import models
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherits from BaseModel """
    state_id = ""
    name = ""
