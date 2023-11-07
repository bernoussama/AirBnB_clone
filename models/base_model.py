#!/usr/bin/python3
"""
    base_model Module
"""

import uuid
from datetime import datetime
import time


class BaseModel:
    def __init__(self) -> None:
        """
        BaseModel constuctor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        this_dict = self.__dict__
        this_dict["__class__"] = self.__class__.__name__
        this_dict["updated_at"] = self.updated_at.isoformat(
            # timespec="%Y-%m-%dT%H:%M:%S.%f"
        )
        this_dict["created_at"] = self.created_at.isoformat(
            # timespec="%Y-%m-%dT%H:%M:%S.%f"
        )
        return this_dict


if __name__ == "__main__":
    bm1 = BaseModel()
    print(f"__str__:{bm1}")
    print(f"to_dict:{bm1.to_dict()}")
