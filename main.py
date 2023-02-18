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
    state.metadata = mt.get_metadata(state.ticker)
    state.revenue = mt.get_revenue(state.ticker)
    state.eps = mt.get_eps(state.ticker)
    state.period = 'Quarterly (FQ)'

# when ticker submit, check validity, clear input and update data
def submit():
    # if invalid ticker dont do anything
    if mt.check_ticker(state.input):
        st.error('No Results Found')
        state.input = ''
    else:
        state.ticker = state.input
        state.input = ''
        state.metadata = mt.get_metadata(state.ticker)
        state.revenue = mt.get_revenue(state.ticker)
        state.eps = mt.get_eps(state.ticker)

st.text_input('.', key='input', placeholder='🔍  Search for a ticker', label_visibility='collapsed', on_change=submit)

with st.sidebar:
    st.header(f'{state.metadata["Industry"]} Top Stocks')
    with st.container():
        st.write('Coming Soon')

st.header(f"{state.ticker.upper()} Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader('Sector')
    st.write(state.metadata['Sector'])
with col2:
    st.subheader('Industry')
    st.write(state.metadata['Industry'])
with col3:
    st.subheader('Market Cap')
    st.write(state.metadata['Market Cap'])

with st.expander('Description'):
    # st.subheader('Description')
    st.caption(state.metadata['Description'])

st.radio('.', ('Quarterly (FQ)', 'Annual (FY)', 'Last 12 Months (LTM)'), key='period', horizontal=True, label_visibility='collapsed')

revenue_tab, eps_tab = st.tabs(['Revenue','EPS'])
with revenue_tab:
    st.bar_chart(state.revenue[state.period])
with eps_tab:
    st.bar_chart(state.eps[state.period])
