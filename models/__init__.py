#!/usr/bin/pythin
"""
updated the init file
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
