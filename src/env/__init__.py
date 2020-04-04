"""Facilities for interacting with the environment."""

from typing import List
import os


def check(keys: List[str]):
    """Raise an error if any of the keys are missing."""
    for key in keys:
        get(key)


def get(name):
    """Get the value of a variable from the environment."""
    val = os.getenv(name)
    if val is None:
        raise Exception(f"Missing required environment variable {name}")
    return val
