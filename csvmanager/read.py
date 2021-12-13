import os

import pandas as pd

class Read:
    @staticmethod
    def DataFrameFromCSVFile(file):
        return pd.read_csv(os.path.abspath(filename))