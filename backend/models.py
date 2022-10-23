from flask import current_app as app
import pandas as pd
import random

quotes = pd.read_csv("quotes_filtered.csv")
memes = pd.read_json("meme_urls.json")
messages = ["remember to hydrate & take a break if you need one :)","hydrate or diedrate","is it time for a 15 minute break yet?", "close your eyes and take a few deep breaths, it's going to be alright <3", "have you meditated yet today? if not, take a few minutes to slow down and ground yourself"]

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