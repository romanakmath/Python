from database.get_yfinance_data import get_yfinance_data
from datetime import datetime as dt


symbol = 'MSFT'
period = '1y'
interval = '1d'
startPoint = "01.01.2025"
endPoint = "31.01.2025"
format_data = "%d.%m.%Y"
startdate = dt.strptime(startPoint, format_data)
enddate = dt.strptime(endPoint, format_data)
get_yfinance_data(symbol, interval= interval, period= period)
