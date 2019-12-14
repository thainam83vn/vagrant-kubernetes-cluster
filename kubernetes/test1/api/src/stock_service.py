from datetime import datetime,timedelta
import time
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

class StockService:
    def getAllSymbols(self):
        df = pd.read_csv('./symbols.csv', sep=':')
        #return list(df["Symbol"])
        return ["AMD", "SNAP", "GPRO", "MDB"]

    def getOnlineSymbols(self):
        return list(pdr.nasdaq_trader.get_nasdaq_symbols()["NASDAQ Symbol"])

    def getQuote(self, symbol, start, end):
        try:
            df = pdr.DataReader(symbol,'yahoo',start,end)
            return df
        except:
            print("Error fetching {}".format(symbol))
            return None

    def analyze(self, df):
        margin = 0.01
        df["Upper"] = df["Close"].rolling(20).mean() + (df["Close"].rolling(20).std()) * 2
        df["Lower"] = df["Close"].rolling(20).mean() - (df["Close"].rolling(20).std()) * 2
        current = df[-1:]
        upper = current["Upper"].item()
        lower = current["Lower"].item()
        close = current["Close"].item()
        #print(upper, close, lower)
        distUpper = (upper*(1-margin) - close)/close
        distLower = (close - lower*(1+margin))/close
        return [round(distUpper,4), round(distLower,4)]

    def suggestions(self):
        end = datetime.today()
        start = end - timedelta(days=365)

        symbols = self.getAllSymbols()
        sales = {}
        buys = {}
        for symbol in symbols:
            df = self.getQuote(symbol, start, end)
            if df is not None:
                distUpper, distLower = self.analyze(df)
                #print(distUpper, distLower)
                if distUpper <= 0:
                    sales[symbol] = distUpper
                if distLower <= 0:
                    buys[symbol] = distLower
            time.sleep(0.3)        
        return {"sales": sales, "buys": buys}