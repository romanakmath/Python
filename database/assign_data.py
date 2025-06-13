from database.get_yfinance_data import get_yfinance_data

def assignDataToSymbolTimeframe(symbolTimeframes):
    tempSymTimeDataList = []
    for symbolTimeframe in symbolTimeframes:
        symbol = symbolTimeframe["symbol"]
        startPoint = symbolTimeframe["start_point"]
        period = symbolTimeframe["period"]
        limit = symbolTimeframe["limit"]
        print("Current active symbols %s" % symbol)

        dataCrypto = use_offline_data(symbol, period, startPoint, limit)
        if not dataCrypto:
            dataCrypto = get_yfinance_data(symbol, period, startPoint)
        else:
            print(dataCrypto)
            dataCrypto = reuse_prev_data(symbol, period, startPoint, limit)

        newSymTimeData = {
                "symbol": symbol,
                "startPoint": startPoint,
                "period": period,
                "limit": limit,
                "data": dataCrypto,
            }
        tempSymTimeDataList.append(newSymTimeData)
    return tempSymTimeDataList
