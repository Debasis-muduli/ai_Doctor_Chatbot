import os
from pathlib import Path
import logging

# Configure logging with timestamp and message format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define list of files to be created
list_of_files = [
    "src/__init__.py",
    "src/helper.py", 
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"  # Fixed extra space before filename
]

# Create files and directories
for filepath in list_of_files:
    # Convert string path to Path object
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir:  # More pythonic check for non-empty string
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create empty file if it doesn't exist or is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass  # Create empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")  # Fixed grammar in message
