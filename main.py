import streamlit as st
import pandas as pd
from macrotrends import MacroTrendsAPI
import time
import datetime as dt

# initialize api used to get data
mt = MacroTrendsAPI()

ticker = st.text_input('.', placeholder='🔍  Search for a ticker', label_visibility='collapsed')

if not ticker:
    ticker = 'AAPL'

# collect data for ticker
revenue = mt.get_quarterly_revenue(ticker)
eps = mt.get_quarterly_eps(ticker)

st.header(f"{ticker.upper()} Dashboard")

period = st.radio('.', ('FQ', 'FY', 'LTM'), horizontal=True, label_visibility='collapsed')

# aggregate data to period
if period == 'FY':
    revenue = revenue.groupby(revenue.index.year).sum()
    eps = eps.groupby(eps.index.year).sum()
elif period == 'LTM':
    pass

revenue_tab, eps_tab = st.tabs(['Revenue','EPS'])
with revenue_tab:
    st.bar_chart(revenue)
with eps_tab:
    st.bar_chart(eps)
