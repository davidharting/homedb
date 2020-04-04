"""
Module for saving and reading files.

Ideally, this would be an abstraction that could read environment variables to determine
where to store files (e.g., S3, Local disk, etc.).
But for now, just reads and writes files to the machine's disk.
"""

import pathlib


def read(dest: str) -> str:
    """
    Read the contents of the file at the destination.
    """
    # For now, assume the destination is a filepath for a filesystem.
    # In the future, it could be an S3 object key as well.
    path = pathlib.Path(dest)
    if path.exists():
        return path.read_text()
    return None


def write(dest: str, contents: str):
    """
    Save the contents to a file at the specified destination.
    """
    path = pathlib.Path(dest)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contents)
