import requests
import json

class Config:
    def __init__(self, url):
        self.URL = url
        self.CURRENCIES = ["ADAUSDT",
"ATOMUSDT",
"BATUSDT",
"BCHUSDT",
"BNBUSDT",
"BTCUSDT",
"DASHUSDT",
"EOSUSDT",
"ETCUSDT",
"ETHUSDT",
"IOSTUSDT",
"IOTAUSDT"
"LINKUSDT"
"LTCUSDT",
"MATICUSDT",
"NEOUSDT",
"ONTUSDT",
"QTUMUSDT",
"RVNUSDT",
"TRXUSDT",
"VETUSDT",
"XLMUSDT",
"XMRUSDT",
"XRPUSDT",
"XTZUSDT",
"ZECUSDT",
"ZILUSDT"]
    

    def loadConfig(self):
        result = requests.get(url=self.URL)
        string = result.text
        
        self.CONFIG = json.loads(string)
        
    def checkConfig(self):
        if self.CONFIG is None:
            print("config is not loaded")
            return [False,"config is not loaded"]
        if self.CONFIG["target_long"] is None         or self.CONFIG["target_short"] is None        or self.CONFIG["stop_loss"] is None        or self.CONFIG["method"] is None        or self.CONFIG["strategies"] is None:
            print("missing element in config")
            return [False,"missing element in config"]
        for i in self.CONFIG["strategies"]:
            if i["cryptocurrency"] is None or i["exchange_currency"] is None or i["neckline_short"] is None or i["neckline_long"] is None:
                print("missing element in one of the strategies")
                return [False,"missing element in one of the strategies"]

            if self.CURRENCIES.__contains__(i["cryptocurrency"]) is False:
                print("a cryptocurrency code is wrong in one of the strategies")
                return [False,"a cryptocurrency code is wrong in one of the strategies"]

            if self.CURRENCIES.__contains__(i["exchange_currency"]) is False:
                print("a exchange currency code is wrong in one of the strategies")
                return [False,"a exchange currency code is wrong in one of the strategies"]
            

