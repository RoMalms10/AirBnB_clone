#!/usr/bin/env python3
"""A module that loads storage"""

from models.engine.file_storage import FileStorage
from .base_model import BaseModel

class_dict = {'BaseModel': BaseModel}

storage = FileStorage()
storage.reload()
