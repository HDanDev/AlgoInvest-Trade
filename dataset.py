from repository import Repository

class Dataset:
    def __init__(self, csv_file):
        self._csv_file = csv_file
        self._dataset = Repository(csv_file).read_csv()
        self._valid_shares = [share for share in self.dataset if share.price > 0]

    @property
    def csv_file(self):
        return self._csv_file

    @csv_file.setter
    def csv_file(self, value):
        self._csv_file = value

    @property
    def dataset(self):
        return self._dataset

    @dataset.setter
    def dataset(self, value):
        self._dataset = value

    @property
    def valid_shares(self):
        return self._valid_shares

    @valid_shares.setter
    def valid_shares(self, value):
        self._valid_shares = value