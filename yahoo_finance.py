# import pandas as pd
# import requests

# class YahooFinanceAPI:
#     """
#     `YahooFinanceAPI` is a class used to scrape data from the Yahoo Finance website.
#     """

#     def __init__(self):
#         # requests session used to get website data
#         self.session = requests.Session()
    
#     def get_historical_prices(self, ticker: str) -> pd.DataFrame:
#         """
#         https://finance.yahoo.com/quote/AAPL/history?period1=0&period2=1676678400&interval=1mo&filter=history&frequency=1mo&includeAdjustedClose=true
#         """
#         return
    
#     def get_estimates(self, ticker: str) -> dict:
#         """
#         """

#         return

# request = requests.get('https://www.barchart.com/stocks/quotes/GLBE/competitors?orderBy=weightedAlpha&orderDir=desc')
# df = pd.read_html(request.text)
# print(df)