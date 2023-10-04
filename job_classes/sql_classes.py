from pandas import read_sql_query
from abc import ABC, abstractmethod
from sys import modules as sys_modules

class SQLInputAbstractClass(ABC):
    def get_data(self):
        return read_sql_query(
            self.query_to_exec,
            self.con
        ).to_dict(
            orient="records"
        )
    
    def __del__(self) -> None:
        self.con.close()

class tSqliteInput(SQLInputAbstractClass):

    def __init__(self, **kwargs):
        """
        Parameters:
        location: string path to sqlite database
        query: SQL query optional
        tablename: tablename
        """
        if "sqlite3" not in sys_modules:
            from sqlite3 import connect as sqlite3connect
        if "os" not in sys_modules:
            from os.path import join as os_path_join
        print(sys_modules)
        self.con = sqlite3connect(
            os_path_join(
                kwargs.get("location")
            )
        )
        if not kwargs.get("query"):
            self.query_to_exec = f'SELECT * from {kwargs.get("tablename")}'
