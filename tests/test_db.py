from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture(scope="class")
def sample():
    return pd.read_csv(Path("tests/resources/sample.csv"))


class TestDatabase:
    def test_connection(self, memdb):
        cursor = memdb.connection.cursor
        assert cursor is not None

    def test_add_table(self, memdb, sample):
        memdb.add_table("accessories", sample)

        cur = memdb.connection.cursor()
        res = cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='accessories';"
        ).fetchall()
        assert res is not None, res

        res = cur.execute("Select * from accessories").fetchall()
        assert res is not None, res
        assert len(res[0]) == 22
