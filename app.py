
# Imports
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import yfinance as yf
import hvplot.pandas
from pathlib import Path
from finta import TA
import matplotlib.pyplot as plt
import quantstats as qs
import itertools
from IPython.display import clear_output
import streamlit as st
from main import test_plot, get_data, get_individual_stock

# global variables

sqrt = np.sqrt(252)
trading_days_year = 252
total_days_year = 365
thirty_years_ago = (pd.Timestamp.today() - pd.Timedelta(days = total_days_year * 30)).date()
ten_years_ago = (pd.Timestamp.today() - pd.Timedelta(days = total_days_year * 10)).date()
five_years_ago = (pd.Timestamp.today() - pd.Timedelta(days = total_days_year * 5)).date()
three_years_ago = (pd.Timestamp.today() - pd.Timedelta(days = total_days_year * 3)).date()
one_year = (pd.Timestamp.today() - pd.Timedelta(days = total_days_year * 1)).date()
six_months = (pd.Timestamp.today() - pd.Timedelta(days = total_days_year / 2)).date()
yesterday = (pd.Timestamp.today() - pd.Timedelta(days = 1)).date()
sixty_days = (pd.Timestamp.today() - pd.Timedelta(days = 59)).date()
# Portfolio vars

share_size = 100
initial_capital = 100000

# Optionable stocks 
optionable_stocks_path = Path('./Resources/optionable_stocks.csv')
with open(optionable_stocks_path, 'r') as file:
    optionable_stocks = file.read()
optionable_stocks = optionable_stocks.replace('\n', ' ')

#user_ticker = st.text_input(label='What ticker would you like to analyze?', max_chars=4, key= 'user_ticker')
#st.write('Pulling YF data')
#stocks_1d = get_data('1d', '2017-01-01', yesterday, optionable_stocks)
#st.write('YF data pulled successfully')



#if st.button("Pull data on this ticker"):
#        ticker_data = get_individual_stock(st.session_state.user_ticker, stocks_1d)
#        st.write(f'{user_ticker} data ready')
#        st.dataframe(ticker_data)
if 'user_ticker' not in st.session_state:
    st.session_state.user_ticker = st.text_input(label='What ticker would you like to analyze?', max_chars=4)
if 'stocks_1d' not in st.session_state:
    st.session_state.stocks_1d = get_data('1d', '2017-01-01', yesterday, optionable_stocks)
st.write('Data pulled successfully')

if st.button("Pull data on this ticker"):
    
    st.session_state.ticker_data = get_individual_stock(st.session_state.user_ticker, st.session_state.stocks_1d)
    st.write(f'{st.session_state.user_ticker} data ready')
    st.write(st.session_state.ticker_data)