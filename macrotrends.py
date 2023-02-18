import requests
import pandas as pd
import utils.format as format
import streamlit as st
import bs4

class MacroTrendsAPI:
    """
    `MacroTrendsAPI` is a class used to scrape data from the MacroTrends website.
    """

    def __init__(self):
        # requests session used to get website data
        self.session = requests.Session()
    
    def get_quarterly_revenue(self, ticker: str) -> pd.DataFrame:
        """
        function used to get quarterly revenue data for ticker.

        example: get_quarterly_revenue('TSLA')

        :param ticker: a valid stock ticker
        :return: a `DataFrame` with columns [date, revenue]
        """
        url = f"https://www.macrotrends.net/stocks/charts/{ticker.upper()}/stock/revenue"
        
        # read table from html into pandas dataframe
        try:
            table_revenue = pd.read_html(url, match='Quarterly Revenue', parse_dates=True)[0]
        except Exception as e:
            st.write(e)
            return []

        # formatting the dataframe
        table_revenue.columns = ['date', 'revenue']
        table_revenue.set_index('date', inplace=True)
        table_revenue = format.columns_price_to_float(table_revenue, ['revenue'])
        table_revenue.sort_index(inplace=True)

        # multiply since table revenue is in millions
        table_revenue['revenue'] *= 1e6

        return table_revenue
    
    def get_quarterly_eps(self, ticker: str) -> pd.DataFrame:
        """
        function used to get quarterly eps data for ticker.

        example: get_quarterly_eps('TSLA')

        :param ticker: a valid stock ticker
        :return: a `DataFrame` with columns [date, eps]
        """
        url = f"https://www.macrotrends.net/stocks/charts/{ticker.upper()}/stock/eps-earnings-per-share-diluted"
        
        # read table from html into pandas dataframe
        try:
            table_eps = pd.read_html(url, match='Quarterly EPS', parse_dates=True)[0]
        except:
            return []

        # formatting the dataframe
        table_eps.columns = ['date', 'eps']
        table_eps.set_index('date', inplace=True)
        table_eps = format.columns_price_to_float(table_eps, ['eps'])
        table_eps.sort_index(inplace=True)

        return table_eps
    
    def get_quarterly_shares_outstanding(self, ticker: str) -> pd.DataFrame:
        """
        """

        return
    
    def get_ttm_gross_margin(self, ticker: str) -> pd.DataFrame:
        """
        """
        
        return
    
    def get_yearly_employee_count(self, ticker: str) -> pd.DataFrame:
        """
        """

        return

if __name__ == "__main__":
    mt = MacroTrendsAPI()

    # # add exception handling to make sure its a stock we can get data for!!! TQQQ is an example

    # tickers = ['net','glbe','shop','sq','nvda','meli','aapl','pypl']
    # for ticker in tickers:
    #     revenue = mt.get_quarterly_revenue(ticker)
        
    #     fig = px.bar(revenue) # make sure the labels work
    #     fig.update_layout(showlegend=False)
    #     fig.show()
