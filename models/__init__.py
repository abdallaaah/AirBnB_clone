import sys
import os

# Get the path to the directory containing this __init__.py file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory (project directory) to sys.path
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

# Now you can import modules from your project directory
from .engine.file_storage import FileStorge

storage = FileStorge()
storage.reload()

