#!/usr/bin/python3
"""User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""


if __name__ == "__main__":
    u = User()
    print(dir(u))
