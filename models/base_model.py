#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """a class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """a constructor to initialize this class

        Args:
            args: input
            kwargs: input
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation of class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the updated_at with cirrent time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates a dictionary in json format"""
        return {
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
            }
