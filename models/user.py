#!/usr/bin/python3
""" My User module """
import models
from models.base_model import BaseModel


class User(BaseModel):
    """ User Class inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
