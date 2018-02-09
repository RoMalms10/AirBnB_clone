#!/usr/bin/python3
import datetime
import uuid


class BaseModel():
    """A BaseModel class to serve as the base of all models"""
    id="None"
    created_at=None
    updated_at=None

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now().isoformat())
        self.updated_at = str(datetime.datetime.now().isoformat())

    def __str__(self):
        """A method that returns a string representation"""
        return "[{}] [{}] {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """A method that returns time instance updated"""
        return self.updated_at

    def to_dict(self):
        """A method that returns a dictionary containing all
            keys/values of __dict__ of the instance"""
        new_dict = {}
        for att in self.__dict__:
            new_dict[att] = getattr(self, att)
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
