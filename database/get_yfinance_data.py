import yfinance as yf
import openpyxl as ox
import pandas as pd
import sqlite3 
from datetime import datetime as dt

def  get_yfinance_data(symbol, interval, period):
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

    #startPointstr = dt.strftime(startPoint, "%Y-%m-%d")

    #start = dt.strptime(f"{startPoint}";, "%Y-%m-%d")  # Avoids leap year bug.
    #end  = dt.strptime(f"{endPoint}";, "%Y-%m-%d")  # Avoids leap year bug.

    #endPointstr = dt.strftime(endPoint, "%Y-%m-%d")

    data = yf.download( list(symbol), period=period , interval=interval)

    data['SYMBOL'] = symbol
    data['interval'] = period

    print(data.head())
    #print(data)
    #print(type(data))
    #print(data['Close'])

    #data.to_csv (r'C:\BckUp\Python\finance.csv', index = None, header=True) 

    # conn = sqlite3.connect('backtest.db')
    # data.to_sql('finance', conn, if_exists='replace')

    # data = yf.download( list(symbol), start=startPointstr, end=endPointstr , interval='1d')
    # data.to_sql('finance_imp', conn, if_exists='replace')



    #conn.execute("""CREATE INDEX finance_symbol ON finance(SYMBOL)""")

    #  data = yf.download(symbol, interval='1d')
    #data['SYMBOL'] = symbol

    #conn = sqlite3.connect('backtest.db')
    # data = yf.download( symbol, start=startPointstr, end=endPointstr , interval=period)
    # data['SYMBOL'] = symbol
    # data['interval'] = period
    # data.to_sql('finance_nolist', conn, if_exists='replace')

       
    #cursor = backtest_db.cursor()
    #cursor.execute("""Insert into finance [feldliste] select [feldliste]  from finance_imp t1 where not exists (select [key] from finance t2 where t1.date = t2.date and t2.symbol =[symbol] and t2.inetravl=[period]""")
    #cursor.fetchone()