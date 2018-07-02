class Line:

    def __init__(self, id, name):
        self.id = id
        self.name = name

        self.articles = []

    def add_article(self, a):
        self.articles.append(a)
        p.lineId = self.id

    def search(self, w):
        for a in articles:
            if a.name == w:
                return a
            else
                return 0
    
    