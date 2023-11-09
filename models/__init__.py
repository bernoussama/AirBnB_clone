#!/usr/bin/python3
<<<<<<< HEAD
"""An instance of the FileStorage class is created in this module"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
=======


from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
>>>>>>> 76b5363d195b5a9bf9fd9a7dc4640b2333668d2f
