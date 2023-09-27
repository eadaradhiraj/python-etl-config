import pandas as pd

class tFileDelimited:

    def __init__(
        self,
        filepath_or_buffer: str,
        lineterminator: str = '\n',
        delimiter: str = ';',
        header: int = 0,
        skipfooter: int = 0
    ):
        self.lineterminator = lineterminator
        self.filepath_or_buffer = filepath_or_buffer
        self.delimiter = delimiter
        self.header = header
        self.skipfooter = skipfooter
    
    def get_data(self):
        return pd.read_csv(
            filepath_or_buffer=self.filepath_or_buffer,
            lineterminator=self.lineterminator,
            delimiter=self.delimiter,
            header=self.header,
            skipfooter=self.skipfooter
        ).to_dict(
            orient=records
        )