import streamlit as st
import pandas as pd
from macrotrends import MacroTrendsAPI

# initialize api
mt = MacroTrendsAPI()

st.header("Stock Dashboard")

ticker = st.text_input('Ticker', 'TSLA')

tab1, tab2 = st.tabs(["Revenue", "EPS"])
with tab1:
    data = mt.get_quarterly_revenue(ticker)
    st.bar_chart(data)
with tab2:
    data = mt.get_quarterly_eps(ticker)
    st.bar_chart(data)