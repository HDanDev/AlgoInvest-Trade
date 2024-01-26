import csv
from share import Share

class Repository:
    def __init__(self, csv_file):
        self._csv_file = csv_file

    @property
    def csv_file(self):
        return self._csv_file

    @csv_file.setter
    def csv_file(self, value):
        self._csv_file = value
    
    def read_csv(self):
        shares = []
        with open(self._csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                share = Share(row['name'], row['price'], row['profit'])
                shares.append(share)
        return shares