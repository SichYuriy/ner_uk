from natasha_uk import NamesExtractor


class NameExtractingService:
    def __init__(self, names_extractor):
        self.names_extractor = names_extractor

    def extract_names(self, articles):
        return list(map(lambda article: self.names_extractor(article), articles))


name_extracting_service = NameExtractingService(NamesExtractor())
