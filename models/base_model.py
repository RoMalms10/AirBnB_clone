#!/usr/bin/python3
"""
A module that handles random id generation, datetime created, datetime
updated, and dictionary instantiation of a BaseModel
    Args:
        none
    Returns:
        instance dictionary
"""
import datetime
import json
import models
import sys
import uuid


class BaseModel():
    """A BaseModel class to serve as the base of all models """

    def __init__(self, *args, **kwargs):
        """Initialize instance random id generation and datetime created"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key not in ["__class__"]:
                    setattr(self, key, value)

    def __str__(self):
        """A method that returns a string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        """A method that returns a string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """A method that updates instance datetime"""
        self.updated_at = datetime.datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """A method that returns a JSON dictionary
           containing all keys/values of __dict__ of the instance"""
        new_dict = {}
        for att in self.__dict__:
            if att in ["created_at", "updated_at"]:
                new_dict[att] = getattr(self, att).isoformat()
            else:
                new_dict[att] = getattr(self, att)
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)
