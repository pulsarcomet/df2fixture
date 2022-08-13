from abc import abstractmethod

import pandas as pd

class BaseMapper:
    @abstractmethod
    def fit(self, series: pd.Series):
        pass

    def predict(self, array: pd.Series) -> pd.Series:
        pass

