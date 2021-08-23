import os

import pandas as pd

from paths import DB_PATH


class CSVDBManager:
    """DB Manager uses file system (.csv)"""

    def __init__(self):
        self.CSV_PATH = DB_PATH / 'db.csv'
        self._data = None
        self._sources = ['job.korea.ac.kr']

    def read_db(self):
        if (not os.path.exists(DB_PATH)) and (not os.path.exists(self.CSV_PATH)):
            os.mkdir(DB_PATH)
            self._data = pd.DataFrame()

        elif (os.path.exists(DB_PATH)) and (not os.path.exists(self.CSV_PATH)):
            self._data = pd.DataFrame()
        else:
            self._data = pd.read_csv(
                self.CSV_PATH, engine='python', index_col=0)

            for source in self._sources:
                self._data = self._preprocess(self._data, source=source)

    def write_db(self):
        self._data.to_csv(self.CSV_PATH)

    def append(self, data: pd.DataFrame, source: str):
        data = self._preprocess(data, source=source)

        if self._data.shape[0] == 0:
            self._data = data

        else:
            for idx in data.index:
                post_id = data.loc[idx, 'post_id']
                if post_id not in self._data['post_id'].tolist():
                    self._data = self._data.append(data.iloc[idx, :])
            self._data = self._data.sort_values(
                by='post_id', ascending=False).reset_index(drop=True)

    def _preprocess(self, data: pd.DataFrame, source: str):
        if source == 'job.korea.ac.kr':
            data['post_id'] = data['post_id'].astype(int)
        else:
            raise NotImplementedError

        return data
