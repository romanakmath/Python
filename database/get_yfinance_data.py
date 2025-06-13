import yfinance as yf
import pandas as pd

def  get_yfinance_data(symbol, period, startPoint):
    dat = yf.Ticker("MSFT")
    dat.info
    dat.calendar
    dat.analyst_price_targets
    dat.quarterly_income_stmt
    dat.history(period='1mo')
    dat.option_chain(dat.options[0]).calls

    pfinancials = dat.financials

    #print(pfinancials)

    print(dat.history(period=period))

    data = yf.download(list(dat), group_by='column', period=period, interval='1d')

    print(data)
    #print(data['Open'])

    

    