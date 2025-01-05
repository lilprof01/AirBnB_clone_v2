#!/usr/bin/pythin
"""
updated the init file
"""
from models.engine import file_storage
from os import getenv



if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
