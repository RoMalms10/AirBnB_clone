#!/usr/bin/env python3
""" My module for file storage """
import json
import models
from models.base_model import BaseModel
import os


class FileStorage():
    """
    """


    __file_storage = "file.json"
    __objects = {}


    def all(self):
        """
        """


        return self.__objects


    def new(self, obj):
        """
        """


        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    def save(self):
        """
        """


        with open(self.__file_storage, mode="w", encoding="UTF-8") as f:
            for key, value in self.__objects.items():
                self.__objects[key] = value.to_dict()
            json.dump(self.__objects, f)


    def reload(self):
        """
        """

        if os.path.isfile(self.__file_storage):
            with open(self.__file_storage, mode="r", encoding="UTF-8") as f:
                temp_dict = json.load(f)
            for key, value in temp_dict.items():
                univ = value.get('__class__')
                if univ in models.class_dict:
                    self.__objects[key] = models.class_dict[univ](**value)
