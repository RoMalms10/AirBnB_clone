#!/usr/bin/python3
""" My module for file storage """
import json
import models
import os


class FileStorage():
    """ Class that deals with file storage and loading """

    __file_storage = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dict containing all objects """
        return self.__objects

    def new(self, obj):
        """ Adds new object to dict of current objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ saves all objects into a JSON file """
        save_dict = {}
        with open(self.__file_storage, mode="w", encoding="UTF-8") as f:
            for key, value in self.__objects.items():
                save_dict[key] = value.to_dict()
            json.dump(save_dict, f)

    def reload(self):
        """ Reloads the JSON from the specified file """
        if os.path.exists(self.__file_storage):
            with open(self.__file_storage, mode="r", encoding="UTF-8") as f:
                temp_dict = json.load(f)
            for key, value in temp_dict.items():
                univ = value.get('__class__')
                if univ in models.class_dict:
                    self.__objects[key] = models.class_dict[univ](**value)
        else:
            pass
