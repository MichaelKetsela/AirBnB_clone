#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""

        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance."""
        redict = self.__dict__.copy()
        redict["created_at"] = self.created_at.isoformat()
        redict["updated_at"] = self.updated_at.isoformat()
        redict["__class__"] = self.__class__.__name__
        return redict

    def __str__(self):
        """Print the BaseModel instance."""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
