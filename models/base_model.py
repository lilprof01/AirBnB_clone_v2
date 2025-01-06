#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String


Base = declarative_base()


class BaseModel:
    """a class that defines all common attributes/methods for other classes"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)    

    def __str__(self):
        """string representation of class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the updated_at with cirrent time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates a dictionary in json format"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)
