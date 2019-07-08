import csv


class Extractor:

    def extract(self, *args, **kwargs):
        pass


class CsvExtractor(Extractor):
    """
    Reads from CSV and returns a list of dicts
    """

    def extract(self, csv_name, *args, **kwargs):
        with open(csv_name, 'r') as input_file:
            reader = csv.DictReader(input_file)
            return [row for row in reader]


class SmartExtractor(Extractor):
    extractors_by_extension = {'csv': CsvExtractor()}

    def extract(self, file_name, *args, **kwargs):
        extension = file_name.split('.')[-1]
        extractor = self.extractors_by_extension[extension]()
        return extractor.extract(file_name, *args, **kwargs)
