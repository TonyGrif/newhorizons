"""This module contains the Database class"""

import sqlite3

import pandas as pd


class Database:
    """This class is responsible for managing the newhorizons db"""

    def __init__(self, mem: bool = False) -> None:
        """Constructor for the newhorizons db"""
        if mem:
            self.connection = sqlite3.connect(":memory:")
            return
        self.connection = sqlite3.connect("newhorizons.db")

    def add_table(self, name: str, frame: pd.DataFrame):
        frame.to_sql(name, self.connection, index=False)
