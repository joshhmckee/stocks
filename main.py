import streamlit as st
import pandas as pd
from macrotrends import MacroTrendsAPI

# make window wide
st.set_page_config(layout="wide")

# initialize api
mt = MacroTrendsAPI()

st.header("Stock Dashboard")

col1, _, _ = st.columns(3)
with col1:
    ticker = st.text_input('Ticker', 'TSLA')

st.write('Graph Selections')
col1, col2 = st.columns(2)
with col1:
    revenue_check = st.checkbox('Revenue')
with col2:
    eps_check = st.checkbox('EPS')

# tab1, tab2 = st.tabs(["Revenue", "EPS"])
# with tab1:
#     data = mt.get_quarterly_revenue(ticker)
#     st.bar_chart(data)
# with tab2:
#     data = mt.get_quarterly_eps(ticker)
#     st.bar_chart(data)

col1, col2, col3 = st.columns(3)
with col1:
    if revenue_check:
        data = mt.get_quarterly_revenue(ticker)
        st.write(data)
with col2:
    if eps_check:
        data = mt.get_quarterly_eps(ticker)
        st.bar_chart(data)
with col3:
    pass