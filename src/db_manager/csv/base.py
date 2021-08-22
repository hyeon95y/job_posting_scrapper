import os

import pandas as pd

from paths import DB_PATH


class CSVDBManager:
    def __init__(self):
        self.CSV_PATH = DB_PATH / 'db.csv'
        self._data = None

    def read_db(self):
        if not os.path.exists(DB_PATH):
            os.mkdir(DB_PATH)
            self._data = pd.DataFrame()
        else:
            self._data = pd.read_csv(
                self.CSV_PATH, engine='python', index_col=0)
            self._data['post_id'] = self._data['post_id'].astype(int)

    def write_db(self):
        self._data.to_csv(self.CSV_PATH)

    def append(self, data: pd.DataFrame):
        data['post_id'] = data['post_id'].astype(int)
        for idx in data.index:
            post_id = data.loc[idx, 'post_id']
            if post_id not in self._data['post_id'].tolist():
                self._data = self._data.append(data.iloc[idx, :])
        self._data = self._data.sort_values(
            by='post_id', ascending=False).reset_index(drop=True)
