class TitleStore:
    titles = []

    @classmethod
    def add_title(cls, title):
        cls.titles.append(title)

    @classmethod
    def get_titles(cls):
        return cls.titles
