from natasha_uk import DatesExtractor


class DateExtractingService:
    def __init__(self, dates_extractor):
        self.dates_extractor = dates_extractor

    def extract_dates(self, articles):
        return list(map(lambda article: self.dates_extractor(article), articles))


date_extracting_service = DateExtractingService(DatesExtractor())
