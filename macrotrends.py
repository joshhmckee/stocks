from xmlrpc.client import boolean
import requests
import pandas as pd
import utils.format as format
import streamlit as st
import time

class MacroTrendsAPI:
    """
    `MacroTrendsAPI` is a class used to scrape data from the MacroTrends website.
    """

    def __init__(self):
        # requests session used to get website data
        self.session = requests.Session()
    
    def check_ticker(self, ticker: str) -> bool:
        """
        function checks if ticker is a valid stock ticker.

        example: check_ticker('TSLA')
        :param: a stock ticker
        :return: true or false depending on if the ticker is valid
        """
        # request website html
        url = f"https://www.macrotrends.net/stocks/charts/{ticker.upper()}/stock/stock-price-history"
        html = self.session.get(url).text
        # check for 404 error in html
        return 'Error Code: 404' in html
    
    def get_revenue(self, ticker: str) -> dict:
        """
        function used to get FQ, FY, LTM revenue data for ticker.

        example: get_revenue('TSLA')

        :param ticker: a valid stock ticker
        :return: a `dict` with period as keys and revenue `DataFrame` as values
        """
        revenue_data = {'Quarterly (FQ)': [], 'Annual (FY)': [], 'Last 12 Months (LTM)': []}
        try:
            # request website html
            url = f"https://www.macrotrends.net/stocks/charts/{ticker.upper()}/stock/revenue"
            html = self.session.get(url).text

            quarter_table = pd.read_html(html, match='Quarterly Revenue', parse_dates=True)[0]
            revenue_data['Quarterly (FQ)'] = format.format_financial_table(quarter_table, 'revenue', '%Y-%m-%d')

            year_table = pd.read_html(html, match='Annual Revenue', parse_dates=True)[0]
            revenue_data['Annual (FY)'] = format.format_financial_table(year_table, 'revenue', '%Y')

            revenue_data['Last 12 Months (LTM)'] = revenue_data['Quarterly (FQ)'].rolling(4).sum()
        except:
            st.error('An Error Occurred')

        return revenue_data
    
    def get_eps(self, ticker: str) -> pd.DataFrame:
        """
        function used to get FQ, FY, LTM eps data for ticker.

        example: get_eps('TSLA')

        :param ticker: a valid stock ticker
        :return: a `dict` with period as keys and eps `DataFrame` as values
        """

        # request website html
        url = f"https://www.macrotrends.net/stocks/charts/{ticker.upper()}/stock/eps-earnings-per-share-diluted"
        html = self.session.get(url).text

        eps_data = {}

        quarter_table = pd.read_html(html, match='Quarterly EPS', parse_dates=True)[0]
        eps_data['Quarterly (FQ)'] = format.format_financial_table(quarter_table, 'eps', '%Y-%m-%d')

        year_table = pd.read_html(html, match='Annual EPS', parse_dates=True)[0]
        eps_data['Annual (FY)'] = format.format_financial_table(year_table, 'eps', '%Y')

        eps_data['Last 12 Months (LTM)'] = eps_data['Quarterly (FQ)'].rolling(4).sum()

        return eps_data

    
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
    url = f"https://www.macrotrends.net/stocks/charts/TSLA/stock/revenue"
    request = requests.get(url)
    df = pd.read_html(request.text, parse_dates=True)
    print(df)
