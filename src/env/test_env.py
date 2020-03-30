"""Test the env package"""

import os
import pytest

import env


@pytest.fixture()
def setup():
    os.environ["SECRET"] = "sshhh"
    yield "wait for teardown"
    del os.environ["SECRET"]


class TestEnvGet:
    def test_raises_exception_when_missing(self):
        with pytest.raises(Exception) as e:
            env.get("API_KEY")
        assert "Missing required" in str(e.value)

    def test_returns_environment_variable(self, setup):
        assert env.get("SECRET") == "sshhh"
