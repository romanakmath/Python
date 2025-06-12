import pandas as pd

def get_dummy_data(symbolTimeframes):
    tempSymTimeDataList = []

    for symbolTimeframe in symbolTimeframes:
        symbol = symbolTimeframe["symbol"]
        startPoint = symbolTimeframe["start_point"]
        period = symbolTimeframe["period"]
        limit = symbolTimeframe["limit"]
        print("Current active symbols %s" % symbol)
        columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
        ohlcv = pd.DataFrame(columns=columns)
        ohlcv_row_values = [pd.Timestamp("2023-03-01"), 1, 10, 1, -1, 5]
        ohlcv = pd.concat(
            [pd.DataFrame([ohlcv_row_values], columns=ohlcv.columns), ohlcv],
            ignore_index=True,
        )
        # set the index
        ohlcv.set_index("Date", inplace=True)
        newSymTimeData = {
            "symbol": symbol,
            "startPoint": startPoint,
            "period": period,
            "limit": limit,
            "data": ohlcv,
        }
        tempSymTimeDataList.append(newSymTimeData)
    return tempSymTimeDataList