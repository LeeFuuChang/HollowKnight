import shutil
import os

for root, dirs, files in os.walk(os.path.dirname(__file__)):
    if "__pycache__" in dirs:
        shutil.rmtree(os.path.join(root, "__pycache__"))