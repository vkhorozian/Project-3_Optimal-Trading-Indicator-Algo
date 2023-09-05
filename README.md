# Project 3:  Expansion on Analysis and Backtesting of Trading Indicators to Identify Optimal Trading Models

This project is a summary of project 1, 2 and 3 analysis insights for our investment research and algo trading strategies.

# Project 3: Goals

1. Data Collection and Processing:
    - Data from projects 1 and 2 are the datasets that will be utilized in project 3.  No additional data is
    required for project 3.
    - Data preprocessing will involve additional analysis and summary of data insights from project 2. 

2. Data Analysis and Trading Insights:
    - Isolate winning trading strategies within the subset population studied.
    - Create portfolio of trades that maximize returns over the time period analyzed.
    - Develop several trading/portfolio strategies depending on investor goals.

3. Digital Trading Analysis Platform (DTAP):
    - Develop a digital trading analysis platform that summarizes:
    - Trading strategy performance by stocks, sectors and indexes
    - Optimal portfolio of trades based on specific investment criteria.
    - Winning portfolio strategies that provide efficient frontier return performance.

**Project 1 Portfolio**:  This is a stock selection quantitative investment research-based portfolio designed to beat market indexes from a return/risk perspective.

**Algo Trading Strategy 1 Portfolio**:  This is an algo trading portfolio selected based on the following criteria:
1.	Best Sharpe ratio algo strategy for each individual stock in our sample (85 optionable stock universe, 85 top algo trading strategy for each stock in sample)
2.	Sharpe ratio > 1 for algo strategy 
3.	Algo strategy Sharpe ratio for the stock beats buy and hold Sharpe ratio for the same stock

**Algo Trading Strategy 2 Portfolio**:  This is an algo trading portfolio selected based on the following criteria:
1.	Best Sharpe ratio algo strategy for each individual stock in our sample (85 optionable stock universe, 85 top algo trading strategy for each stock in sample)
2.	Sharpe ratio > 1.1 for algo strategy 
---

### **Stocks in Portfolio:**

| Project 1 Portfolio       | Project 3 Algo Strategy 1 Portfolio | Project 3 Algo Strategy 2 Portfolio |
|--------------------------|------------------------------------|------------------------------------|
| MSFT                     | CAH                                | AAPL                               |
| NVDA                     | CSX                                | CAH                                |
| AAPL                     | MARA                               | CSX                                |
| GE                       | MPC                                | HD                                 |
| DHI                      | MRNA                               | MPC                                |
| CAH                      | MSFT                               | MRNA                               |
| AFL                      | NKE                                | NVDA                               |
| JPM                      | NVDA                               | PLUG                               |
| MS                       | PLUG                               | TSLA                               |
| ORCL                     | TSLA                               |                                    |
| MRK                      |                                    |                                    |
| MPC                      |                                    |                                    |

---
### **Key Indicators in Algorithmic Trading Portfolio 1 – Buy Signals:**

| Stock | EMA 20 | EMA 50 | Squeeze | Chaikin | MACD | MFI | # of Indicators |
|-------|--------|--------|---------|---------|------|-----|-----------------|
| CAH   |        |        |    x    |         |      |  x  |        2        |
| CSX   |        |        |    x    |         |      |  x  |        2        |
| MARA  |    x   |        |         |         |      |     |        1        |
| MPC   |        |        |         |         |   x  |     |        1        |
| MRNA  |    x   |    x   |         |         |      |     |        2        |
| MSFT  |    x   |    x   |         |         |      |     |        2        |
| NKE   |        |    x   |         |         |      |     |        1        |
| NVDA  |        |        |    x    |    x    |   x  |     |        3        |
| PLUG  |        |    x   |    x    |         |   x  |     |        3        |
| TSLA  |    x   |    x   |         |         |   x  |     |        3        |
| VLO   |    x   |        |         |         |      |     |        1        |

### Used
- EMA 20: 5/11
- EMA 50: 5/11
- Squeeze: 4/11
- Chaikin: 1/11
- MACD: 4/11
- MFI: 2/11
---
### **Key Indicators in Algorithmic Trading Portfolio 1 – Sell Signals:**

| Stock | BB-Bands | MACD | ADX | EMA 20 | # of Indicators |
|-------|----------|------|-----|--------|-----------------|
| CAH   |    x     |      |  x  |        |        2        |
| CSX   |    x     |      |     |        |        1        |
| MARA  |    x     |  x   |     |        |        2        |
| MPC   |          |  x   |     |        |        1        |
| MRNA  |    x     |      |     |    x   |        2        |
| MSFT  |    x     |      |     |        |        1        |
| NKE   |    x     |      |  x  |        |        2        |
| NVDA  |    x     |      |     |        |        1        |
| PLUG  |    x     |  x   |     |        |        2        |
| TSLA  |          |  x   |     |    x   |        2        |
| VLO   |    x     |  x   |     |        |        2        |

### Used
- BB-Bands: 9/11
- MACD: 5/11
- ADX: 2/11
- EMA 20: 2/11
---
### **Key Indicators in Algorithmic Trading Portfolio 2 – Buy Signals:**

| Stock | EMA 20 | EMA 50 | Squeeze | Chaikin | MACD | MFI | # of Indicators |
|-------|--------|--------|---------|---------|------|-----|-----------------|
| AAPL  |   x    |        |         |         |   x  |     |        2        |
| CAH   |        |        |    x    |         |      |  x  |        2        |
| CSX   |        |        |         |         |      |  x  |        1        |
| HD    |   x    |   x    |         |    x    |      |     |        3        |
| MPC   |        |        |         |         |   x  |     |        1        |
| MRNA  |        |    x   |         |         |      |     |        1        |
| NVDA  |   x    |        |         |         |   x  |     |        2        |
| PLUG  |   x    |   x    |    x    |         |      |     |        3        |
| TSLA  |   x    |   x    |         |         |   x  |     |        3        |

### Used
- EMA 20: 5/9
- EMA 50: 4/9
- Squeeze: 2/9
- Chaikin: 1/9
- MACD: 4/9
- MFI: 2/9

---
### **Key Indicators in Algorithmic Trading Portfolio 2 – Sell Signals:**


| Stock | BB-Bands | MACD | ADX | EMA 20 | # of Indicators |
|-------|----------|------|-----|--------|-----------------|
| AAPL  |          |  x   |     |        |        1        |
| CAH   |    x     |      |  x  |        |        2        |
| CSX   |    x     |      |     |        |        2        |
| HD    |          |  x   |     |    x   |        1        |
| MPC   |          |  x   |     |        |        2        |
| MRNA  |    x     |      |     |    x   |        1        |
| NVDA  |          |      |     |    x   |        2        |
| PLUG  |    x     |  x   |     |        |        1        |
| TSLA  |          |  x   |     |    x   |        2        |

### Used
- BB-Bands: 4/9
- MACD: 5/9
- ADX: 1/9
- EMA 20: 4/9

### **Top Entry Signals Use:**
    •	EMA 20
    •	EMA 50
    •	Squeeze
    •	MACD

### **Top Exit Signals Use:**
    •	Bollinger Bands (by far)
    •	MACD
    •	EMA 20
    -----------------------------
    1. All Algo trading models simplistic in they only use 2-3 indicators.
    2. Entry Indicators are different than exit indicators, the same indicator is not useful in both scenarios.

## Returns, Risk Analysis Insights by Portfolio:

### **Project 1 Portfolio:**
    • Clearly this portfolio is producing solid risk adjusted returns and Sharpe ratios that are beating both market indexes.

### **Algo Strategy 1 Portfolio:**
    • The first chart shows us a comparison of Sharpe Ratios and volatility for algo trading strategies and buy and hold strategies for the same 11 stocks.  We can clearly see algo value in driving down risk and driving up returns (blue dots vs. red dots)
    • In this portfolio, every individual stock has an algo strategy that beats buy and hold (2nd bar chart)
    • An annualized returns/volatility chart also shows us how the algo strategy stocks are producing more efficient returns vs. the same stocks in a buy and hold strategy.  The linear relationship between annual returns and volatility is also very interesting

### **Algo Strategy 2 Portfolio:**
    • The first chart shows us a comparison of Sharpe Ratios and volatility for algo trading strategies and buy and hold strategies for the same 9 stocks.  In this 2nd portfolio, we can again see algo value in driving down risk and driving up returns (blue dots vs. red dots)
    • In this portfolio, every individual stock does not have an algo strategy that beats buy and hold (2nd bar chart).  We have high Sharpe ratio stocks where buy and hold beat algo strategy performance (AAPL, NVDA, HD)
    • An annualized returns/volatility chart in general, shows us how the algo strategy stocks are producing more efficient returns vs. the same stocks in a buy and hold strategy. 


--------------
## Notebooks
- [JUPYTER LAB NOTEBOOK LINK](./main.ipynb)
- [Final Analysis](./README.md)
---------

## Getting Started - Prerequisites
---
### ​You must have Python 3 installed:

```
python3 --version
```

### You must have Anaconda installed:
```
$ anaconda --version
```

### Install Environmnet:
```
conda create -n <env_name> python=3.7 anaconda
```

### Clone/Run Repository 
```
git clone git@github.com:vkhorozian/Project-3.git
```

### Activate Environment
```
conda activate <env_name>
```

### Install Dependencies
- Please make sure you are in your intended activate environment before running this command
```
pip install -r requirements.txt
```

--- 

## Built With

- [![Python 3.7.13](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)]([https://www.python.org/downloads/release/python-3713/)
[![Python](https://img.shields.io/badge/Python-3.7.13-blue)](https://www.python.org/downloads/release/python-3713/) - Programming Language
- [![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/docs/#) - Data maniupulation library
- [![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/) - Multi-dimensional array library
- [![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/) - Visualization library for plots
- [![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/) - Visualization library for plots
- [![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=plotly&logoColor=white)](https://seaborn.pydata.org/) - Visualization library for plots
- [![Alpaca](https://img.shields.io/badge/Alpaca-3776AB?style=for-the-badge&logo=plotly&logoColor=white)](https://alpaca.markets/) - Trading API
- [![HVPlot](https://img.shields.io/badge/HVPlot-3776AB?style=for-the-badge&logo=plotly&logoColor=white)](https://hvplot.holoviz.org/) - Visualization library for plots
- [![PyViz](https://img.shields.io/badge/PyViz-3776AB?style=for-the-badge&logo=plotly&logoColor=white)](https://pyviz.org/) - Visualization library for plots
- [![GeoViews](https://img.shields.io/badge/GeoViews-3776AB?style=for-the-badge&logo=plotly&logoColor=white)](https://geoviews.org/) - Visualization library for plots
- [![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)](https://jupyter.org/) - Notebook IDE
- [![JupyterLab](https://img.shields.io/badge/JupyterLab-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)](https://jupyter.org/) - Notebook IDE
- [![Anaconda](https://img.shields.io/badge/Anaconda-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com/) - Data science platform
- [![Yahoo Finance API](https://img.shields.io/badge/Yahoo%20Finance%20API-800080?style=for-the-badge&logo=yahoo&logoColor=white)](https://pypi.org/project/yfinance/) - Yahoo Finance API
- [![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/) - Machine learning library
- [![Quantstats](https://img.shields.io/badge/Quantstats-800080?style=for-the-badge&logo=yahoo&logoColor=white)](https://pypi.org/project/quantstats/) - Quantstats library
- [![PyPortfolioOpt](https://img.shields.io/badge/PyPortfolioOpt-800080?style=for-the-badge&logo=yahoo&logoColor=white)](https://pypi.org/project/pyportfolioopt/) - PyPortfolioOpt library
- [![Cufflinks](https://img.shields.io/badge/Cufflinks-800080?style=for-the-badge&logo=yahoo&logoColor=white)](https://pypi.org/project/cufflinks/) - Cufflinks library

---

## Authors
- **Kirill Chugunov** - [LinkedIn](https://www.linkedin.com/in/kirill-chugunov-b680811a4/) | [Github](https://github.com/OddMerchantStudios)
- **Hiren Patel** - [LinkedIn](https://www.linkedin.com/in/hdpatel/) | [Github](https://github.com/hpnhs25)
- **Varoujan John Khorozian** - [LinkedIn](https://www.linkedin.com/in/varoujan-khorozian/) | [Github](https://github.com/vkhorozian)
