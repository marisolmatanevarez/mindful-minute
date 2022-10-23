from flask import current_app as app
import pandas as pd
import random

quotes = pd.read_csv("quotes.csv")
memes = pd.read_json("meme_urls.json")
messages = ...

class Quote():
    def __init__(self, quote, author, category):
        self.quote = quote
        self.author = author
        self.category = category
    
    @staticmethod
    def get_random():
        i = random.randint(0, len(quotes))
        return quotes["quote"][i] + " — " + quotes["author"][i]
    
class Meme():
    def __init__(self, url):
        self.url = url
    
    @staticmethod
    def get_random():
        i = random.randint(0, len(memes))
        return memes[0][i]

class Message():
    def __init__(self, text):
        self.text = text
    
    @staticmethod
    def get_random():
        i = random.randint(0, len(messages))
        return messages[i]