import pandas as pd

from df2fixture.mappers import BaseMapper

class IdMapper(BaseMapper):
    id_map = dict()

    def fit(self, array: pd.Series):
        for i, x in enumerate(array.unique()):
            self.id_map[x] = i+1

    def predict(self, array: pd.Series) -> pd.Series:
        return pd.Series(array).replace(self.id_map)
