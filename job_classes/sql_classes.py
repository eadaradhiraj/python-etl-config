import pandas as pd
import sqlite3
import os

class tsqlite:

    def __init__(self, **kwargs):
        self.con = sqlite3.connect(
            os.path.join(
                kwargs.get("location")
            )
        )
        if not kwargs.get("query"):
            self.query_to_exec = f'SELECT * from {kwargs.get("tablename")}'


    def get_data(self):
        return pd.read_sql_query(
            self.query_to_exec,
            self.con
        ).to_dict(
            orient="records"
        )

    def __del__(self) -> None:
        self.con.close()