able File  7 lines (5 sloc)  162 Bytes
#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
