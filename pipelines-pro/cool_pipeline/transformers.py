class Transformers:

    def transform(self, dirty_data):
        pass


class IronhackTransformer(Transformers):

    def transform(self, dirty_data):
        clean_data = self.clean_data(dirty_data)
        analized_data = self.analyze_data(clean_data)
        return analized_data

    def clean_data(self, dirty_data):
        pass

    def analyze_data(self, clean_data):
        pass

class NullFilterTransformer(IronhackTransformer):

    def clean_data(self, dirty_data):
        return dirty_data # With no null


class CustomVehicleTransformer(IronhackTransformer):

    def clean_data(self, dirty_data):
        years = 2016
        filtered = dirty_data[dirty_data['Year'] == years]
        return filtered

    def analyze_data(self, clean_data):
        grouped = clean_data.groupby('Make').agg({'Combined MPG': 'mean'}).reset_index()
        results = grouped.sort_values('Combined MPG', ascending=False).head(10)
        return results
