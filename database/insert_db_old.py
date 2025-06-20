# import pandas_datareader as web


import yaml
from database.dict_ops import dict_multiassign, getSymbolTimeframes


# from async_appwrite.async_client import AsyncClient
# from async_appwrite.services.async_users import AsyncUsers
from database.dummy_data import get_dummy_data
from database.db import Timeseries, backtest_db

opt_config = yaml.safe_load(open("database/config.yml"))


symbolTimeframesToOpt = getSymbolTimeframes(opt_config["main_opt_config"])
# st_dataList = assignDataToSymbolTimeframe(symbolTimeframesToOpt)


st_dataList = get_dummy_data(symbolTimeframesToOpt)


for symTimeData in st_dataList:
    data = []
    symbol = symTimeData["symbol"]
    for row in symTimeData["data"].itertuples():
        rowDict = row._asdict()
        timestamp_index = rowDict["Index"]


        dt_object = timestamp_index.to_pydatetime()


        ts_dict = {}
        dict_multiassign(
            ts_dict,
            ["symbol", "date", "open", "high", "low", "close", "volume"],
            [
                symbol,
                dt_object,
                rowDict["Open"],
                rowDict["High"],
                rowDict["Low"],
                rowDict["Close"],
                rowDict["Volume"],
            ],
        )


        data.append(ts_dict)


    with backtest_db.atomic():
        query = Timeseries.insert_many(data)
        query.execute()
    
cursor = backtest_db.cursor()
cursor.execute("""Update crypto_tseries set low=12""")
cursor.close()

cursor = backtest_db.cursor()
cursor.execute("""SELECT symbol from crypto_tseries""")
cursor.fetchone()

for x in cursor:
    print(x)
cursor.close()

cursor2 = backtest_db.cursor()
cursor2.execute("""SELECT symbol, date from crypto_tseries""")
cursor2.fetchone()

for x in cursor2:
    print(x)
    print(x[0])
cursor2.close()

cursor2 = backtest_db.cursor()
cursor2.execute("""SELECT symbol from crypto_tseries""")
row=cursor2.fetchall()

for x in row:
    print(x)
cursor2.close()

cursor2 = backtest_db.cursor()
cursor2.execute("""SELECT symbol, date from crypto_tseries""")
row=cursor2.fetchall()

for x in row:
    print(x[0])
    print(x[1])
cursor2.close()