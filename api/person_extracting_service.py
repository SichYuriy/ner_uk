from natasha_uk import PersonExtractor


class PersonExtractingService:
    def __init__(self, person_extractor):
        self.person_extractor = person_extractor

    def extract_persons(self, articles):
        return list(map(lambda article: self.person_extractor(article), articles))


person_extracting_service = PersonExtractingService(PersonExtractor())
