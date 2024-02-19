#!/usr/bin/python3
"""
This module instantiates an object of storage depending on type
Contains the model of all objects
"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()

