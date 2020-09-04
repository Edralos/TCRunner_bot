import requests
import json

class Config:
    def __init__(self, url):
        self.URL = url
    

    def loadConfig(self):
        result = requests.get(url=self.URL)
        string = result.text
        self.CONFIG = json.loads(string)
        

