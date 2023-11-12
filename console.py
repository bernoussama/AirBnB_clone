#!/usr/bin/python3
""" console module for airbnb clone project"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
import models
import inspect
import sys


def get_classes():
    return [
        name
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if inspect.isclass(obj)
    ]


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in get_classes():
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
