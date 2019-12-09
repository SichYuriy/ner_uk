from natasha_uk import LocationExtractor


class LocationExtractingService:
    def __init__(self, locations_extractor):
        self.locations_extractor = locations_extractor

    def extract_locations(self, articles):
        return list(map(lambda article: self.locations_extractor(article), articles))


location_extracting_service = LocationExtractingService(LocationExtractor())
