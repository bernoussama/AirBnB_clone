#!/usr/bin/python3
""" console module for airbnb clone project"""

import cmd
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

if __name__ == '__main__':
    HBNBCommand().cmdloop()