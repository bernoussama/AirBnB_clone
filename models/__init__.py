#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
