class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.description = None
        self.illustration = None

    def __str__(self):
        return f"{self.title} by {self.author}"
