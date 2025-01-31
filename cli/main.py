"""This module contains the main script for creating the newhorizons sqlite3 database"""

import argparse
from pathlib import Path

import pandas as pd

from database import Database


def main():
    """Main drive for database creation"""

    _ = argparse.ArgumentParser(
        prog="New Horizons",
        description="Create a Animal Crossing New Horizons database containing item data",
        epilog="GitHub: https://github.com/TonyGrif/newhorizons",
    )

    db = Database()

    csv_files = Path("data/").glob("*.csv")
    for file in csv_files:
        df = pd.read_csv(file)
        db.add_table(file.stem, df)

    db.connection.close()


if __name__ == "__main__":
    main()
