"""Test the env package"""

import os
import pytest

import env


@pytest.fixture()
def setup():
    """Set the SECRET environment variable before each test, and remove it after."""
    os.environ["SECRET"] = "sshhh"
    yield "wait for teardown"
    del os.environ["SECRET"]


def test_get_raises_exception_when_missing():
    with pytest.raises(Exception) as ex:
        env.get("API_KEY")
    assert "Missing required" in str(ex.value)


@pytest.mark.usefixtures("setup")
def test_get_returns_environment_variable():
    assert env.get("SECRET") == "sshhh"
