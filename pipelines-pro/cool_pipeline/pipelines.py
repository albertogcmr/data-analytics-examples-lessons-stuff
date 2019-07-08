from cool_pipeline.extractors import Extractor, CsvExtractor
from cool_pipeline.loaders import FileLoader, MySQLLoader
from cool_pipeline.transformers import CustomVehicleTransformer, NullFilterTransformer


class Pipeline:

    def run(self):
        pass


class ETLPipeline(Pipeline):
    extractor = Extractor()
    transformers = []
    loaders = []

    def run(self):
        data = self.extractor.extract()
        for transformer in self.transformers:
            data = transformer.transform(data)

        for loader in self.loaders:
            loader.load(data)


class CustomETLPipeline(ETLPipeline):
    extractor = CsvExtractor('./data sets/vehicles/vehicles.csv')
    transformers = [NullFilterTransformer(), CustomVehicleTransformer()]
    loaders = [FileLoader(), MySQLLoader()]
