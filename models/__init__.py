import sys
import os
from .engine.file_storage import FileStorage
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)
storage = FileStorage()
storage.reload()
