from flask import current_app as app

class Quote():
    def __init__(self, quote, author, category):
        self.quote = quote
        self.author = author
        self.category = category
        