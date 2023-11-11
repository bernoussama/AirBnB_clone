#!/usr/bin/python3
"""
    base_model Module
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        BaseModel constuctor
        """

        if kwargs:
            self.updated_at = datetime.fromisoformat(kwargs.get("updated_at"))
            self.created_at = datetime.fromisoformat(kwargs.get("created_at"))
            self.id = kwargs["id"]
        else:
            from models import storage

            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            # time when this function is called
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        this_dict = self.__dict__.copy()
        this_dict["__class__"] = self.__class__.__name__
        this_dict["updated_at"] = self.updated_at.isoformat()
        this_dict["created_at"] = self.created_at.isoformat()
        return this_dict


if __name__ == "__main__":
    bm1 = BaseModel()
    # print(f"__str__:{bm1}")

    bm1_dict = bm1.to_dict()

    bm2 = BaseModel(**bm1_dict)
    print(bm2)
