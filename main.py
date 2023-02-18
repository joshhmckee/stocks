import streamlit as st
import pandas as pd
from macrotrends import MacroTrendsAPI

# initialize api
mt = MacroTrendsAPI()

st.header("Stock Dashboard")

ticker = st.text_input('Ticker', 'TSLA')

revenue_tab, eps_tab = st.tabs(2)
with revenue_tab:
    data = mt.get_quarterly_revenue(ticker)
    st.bar_chart(data)
with eps_tab:
    data = mt.get_quarterly_eps(ticker)
    st.bar_chart(data)
    