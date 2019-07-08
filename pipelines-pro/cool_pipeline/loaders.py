import json


class Loader:

    def load(self, transformed_data):
        pass


class FileLoader(Loader):

    def load(self, transformed_data):
        with open("analized_data.json", 'w') as output_file:
            json.dump(transformed_data, output_file, sort_keys=True, indent=4)

class MySQLLoader(Loader):

    def load(self, transformed_data):
        pass