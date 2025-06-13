from database.get_yfinance_data import get_yfinance_data
import datetime as d


symbol = 'Microsft'
startPoint = '01.01.2025'
period = '1m'
get_yfinance_data(symbol, period, startPoint)
