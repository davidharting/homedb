"""Facilities for interacting with the environment."""

import os


def get(name):
    """Get the value of a variable from the environment."""
    val = os.getenv(name)
    if val is None:
        raise Exception(f"Missing required environment variable {name}")
    return val
