# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:03:38 2023

@author: cuu225
"""

def get종목(wantedDate : str) :

    tickers = stock.get_market_ticker_list(wantedDate, market="KOSDAQ")
    
    for ticker in stock.get_market_ticker_list():
        종목 = stock.get_market_ticker_name(ticker)
    
    return 종목