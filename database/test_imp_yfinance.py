from database.get_yfinance_data import get_yfinance_data
import datetime as d


symbol = 'Microsoft'
period = '1m'
startPoint = '01.01.2025'
get_yfinance_data(symbol, period, startPoint)
