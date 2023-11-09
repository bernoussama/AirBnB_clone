#!/usr/bin/python3

import json


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
        print(the_key)
        self.__objects[the_key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        filename = self.__file_path
        with open(filename, "w") as f:
            # json.dump(self.__objects, f)
            json.dump(
                {
                    k: v.to_dict() if not isinstance(v, dict) else v
                    for k, v in self.__objects.items()
                },
                f,
            )

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except (FileNotFoundError, FileExistsError):
            pass
