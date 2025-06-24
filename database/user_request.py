from database.get_yfinance_data import get_yfinance_data
from datetime import datetime as dt
import yfinance as yf
import calendar
import sqlite3
import pytickersymbols as pyt
from database.db import backtest_db, Timeseries
import pandas as pd
from sqlite3 import connect

from datetime import datetime, timedelta

from database.insert_db import ins_data

from database.check_timeframe import check_data
from database.test_imp_yfinance import imp_yfinance

# print('Enter start (yyyy-mm-dd):')
# check_start = input()

# print('Enter end (yyyy-mm-dd):')
# check_end = input()


check_start = "2024-08-06"
check_end =  "2024-08-21"
Check_OK = True

Check_OK = check_data(check_start, check_end)

sql = "select * from crypto_tseries"
conn =  connect("backtest.db")

if Check_OK:
    df = pd.read_sql(sql, conn)
    print(df)
else:  
    imp_yfinance(check_start, check_end)   
    
    Check_OK = True
    Check_OK = check_data(check_start, check_end)

    if Check_OK:
        df = pd.read_sql(sql, conn)
        print(df)
    else:
        print("Daten in yFinance unvollständig")

conn.close