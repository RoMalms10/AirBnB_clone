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
import uuid


class BaseModel():
    """A BaseModel class to serve as the base of all models"""
    id = "None"
    created_at = None
    updated_at = None

    def __init__(self):
        """Initialize instance random id generation and datetime created"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()

    def __str__(self):
        """A method that returns a string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """A method that updates instance datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """A method that returns a dictionary containing all
           keys/values of __dict__ of the instance"""
        new_dict = {}
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
        for att in self.__dict__:
            new_dict[att] = getattr(self, att)
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
