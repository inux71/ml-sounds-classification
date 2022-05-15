import pandas as pd

class DataFrameFactory:
    def __init__(self) -> None:
        self.data_frame = pd.DataFrame()

    def add_column(self, name: str):
        self.data_frame[name] = None
        return self

    def build(self) -> pd.DataFrame:
        return self.data_frame