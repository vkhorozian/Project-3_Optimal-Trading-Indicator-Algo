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

def test_plot(df):
    # Generate your plot using hvplot
    return df.hvplot()

# this pulls YF data and ranks it
def get_data(interval, start, end, optionable_stocks, seg_window = 21):
    yf_df = yf.Tickers(optionable_stocks)
    df_full =yf_df.history(start = start, end = end, interval= interval)
    stocks = df_full[['Open', 'Close', 'High', 'Low', 'Volume']]
    
    if interval == '5m':
        sqrt_val = 252 * 78 
    elif interval == '15m':
        sqrt_val = 252 * 26  
    elif interval == '30m':
        sqrt_val = 252 * 13 
    elif interval == '1h':
        sqrt_val = 252 * 6.5
    elif interval == '1d':
        sqrt_val = 252
    elif interval == '1wk':
        sqrt_val = 52
        
    stock_names = stocks.columns.get_level_values(1).unique().tolist()

    cumulative_return_column = pd.MultiIndex.from_product([['Rolling_Cumulative_Return'], stock_names])
    volatility_column = pd.MultiIndex.from_product([['Rolling_Volatility'], stock_names])
    sharpe_column = pd.MultiIndex.from_product([['Rolling_Sharpe'], stock_names])
    rank_column = pd.MultiIndex.from_product([['Rank_Sharpe'], stock_names])
    
    df_cumulative_return = pd.DataFrame(0.0, index = stocks.index , columns = cumulative_return_column)
    df_volatility = pd.DataFrame(0.0, index = stocks.index , columns = volatility_column )
    df_sharpe = pd.DataFrame(0.0, index = stocks.index , columns = sharpe_column)
    df_rank = pd.DataFrame(0.0, index = stocks.index , columns = sharpe_column)
    
    for stock in stock_names:
        mask = stocks.columns.get_level_values(1) == stock
        data = stocks.loc[:, mask]
        data.columns = data.columns.droplevel(1)
        close = data['Close']
        returns = data['Close'].pct_change()
        df_cumulative_return[('Rolling_Cumulative_Return', stock)] = (1 + returns).rolling(window=seg_window).apply(lambda x: x.prod())
        df_volatility[('Rolling_Volatility', stock)] = returns.rolling(window=seg_window).std() * np.sqrt(sqrt_val)
        df_sharpe[('Rolling_Sharpe', stock)] = (returns.rolling(window=seg_window).mean() * sqrt_val) / df_volatility[('Rolling_Volatility', stock)]
        
    def rank_row(row):
        return row.rank(ascending=False)

    df_rank = df_sharpe.apply(rank_row, axis=1)
    df_rank.columns = rank_column
    
    final_df = pd.concat([stocks, df_rank], axis = 1)
    
    return final_df

# this slices out individual stock data from the whole df
def get_individual_stock(stock, stocks):
    mask = stocks.columns.get_level_values(1) == stock
    data = stocks.loc[:, mask]
    data.columns = data.columns.droplevel(1)
    data.dropna(inplace = True)
    return data