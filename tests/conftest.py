import pytest

from database import Database


@pytest.fixture(scope="session")
def memdb():
    return Database(mem=True)
