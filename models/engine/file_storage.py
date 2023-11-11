#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        the_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[the_key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        filename = self.__file_path
        try:
            with open(filename, "w", encoding="utf-8") as f:
                # json.dump(self.__objects, f)
                try:
                    json.dump(
                        {
                            k: v.to_dict() if isinstance(v, BaseModel) else v
                            for k, v in self.__objects.items()
                        },
                        f,
                    )
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError to handle: {e}")
                    return
        except (FileNotFoundError, FileExistsError):
            return

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                dicts = json.load(f)
        except (FileNotFoundError, FileExistsError):
            return

        for _, v in dicts.items():
            obj = BaseModel(**v)
            self.new(obj)
