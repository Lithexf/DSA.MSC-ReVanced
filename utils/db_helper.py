import sqlite3
from configparser import ConfigParser
import logging
import pandas as pd
from settings_parser import Settings


class UserData:
    def __init__(self, DEBUG: bool = False) -> None:
        # Connect to the SQLite database
        self.selected_columns = Settings().load_selected_columns()

        conn = sqlite3.connect('data/data.db')

        # Write a SQL query
        if DEBUG:
            print(f"SELECT {", ".join(self.selected_columns)} FROM dsa")
        query = f"SELECT {", ".join(self.selected_columns)} FROM dsa"

        # Read the data into a pandas DataFrame
        self.df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()


if __name__ == '__main__':
    data = UserData()
    print(data.df.head(5))