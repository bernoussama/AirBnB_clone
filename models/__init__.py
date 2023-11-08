#!/usr/bin/python3
"""An instance of the FileStorage class is created in this module"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()