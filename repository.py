import json


class Repository:
    def __init__(self, json_file):
        self._json_file = json_file

    @property
    def json_file(self):
        return self._json_file

    @json_file.setter
    def json_file(self, value):
        self._json_file = value

    def read_json(self):
        with open(self._json_file, 'r') as file:
            data = json.load(file)
        return data