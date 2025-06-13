import yfinance as yf
import openpyxl as ox
import pandas as pd
import sqlite3 

def  get_yfinance_data(symbol, period, startPoint):
    #  dat = yf.Ticker("MSFT")
    # # dat.info
    # # dat.calendar
    # # dat.analyst_price_targets
    # # dat.quarterly_income_stmt
    # # dat.history(period='1mo')
    # # dat.option_chain(dat.options[0]).calls

    #  pfinancials = dat.financials

     #print(pfinancials)

    # print(dat.history(period=period))

    data = yf.download(list(symbol), interval='1d')

    #print(data)
    #print(type(data))
    #print(data['Close'])

    #data.to_csv (r'C:\BckUp\Python\finance.csv', index = None, header=True) 

    conn = sqlite3.connect('backtest.db')
    data.to_sql('finance', conn, if_exists='replace')

    

    