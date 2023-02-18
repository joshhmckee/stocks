import streamlit as st
import pandas as pd
from macrotrends import MacroTrendsAPI
import time
from streamlit import session_state as state

# initialize api used to get data
mt = MacroTrendsAPI()

# default values when app first loaded
if 'ticker' not in state:
    state.ticker = 'AAPL'
    state.revenue = mt.get_revenue(state.ticker)
    state.eps = mt.get_eps(state.ticker)
    state.period = 'Quarterly (FQ)'

# when we submit new ticker, check validity, clear input and update data
def submit():
    # if invalid ticker dont do anything
    if mt.check_ticker(state.input):
        st.error('No Results Found')
        state.input = ''
    else:
        state.ticker = state.input
        state.input = ''
        state.revenue = mt.get_revenue(state.ticker)
        state.eps = mt.get_eps(state.ticker)

st.text_input('.', key='input', placeholder='🔍  Search for a ticker', label_visibility='collapsed', on_change=submit)

st.header(f"{state.ticker.upper()} Dashboard")

st.radio('.', ('Quarterly (FQ)', 'Annual (FY)', 'Last 12 Months (LTM)'), key='period', horizontal=True, label_visibility='collapsed')

revenue_tab, eps_tab = st.tabs(['Revenue','EPS'])
with revenue_tab:
    st.bar_chart(state.revenue[state.period])
with eps_tab:
    st.bar_chart(state.eps[state.period])
