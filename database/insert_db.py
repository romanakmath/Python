# import pandas_datareader as web


import yaml
from database.dict_ops import dict_multiassign, getSymbolTimeframes


# from async_appwrite.async_client import AsyncClient
# from async_appwrite.services.async_users import AsyncUsers
from database.dummy_data import get_dummy_data
from database.db import Timeseries, backtest_db

def ins_data(st_dataList, ticker):

    opt_config = yaml.safe_load(open("database/config.yml"))

    symbol= ticker

    for symTimeData in st_dataList.itertuples():
        rowDict = symTimeData._asdict()
        data = []
        #for row in symTimeData["data"].itertuples():
        #rowDict = row._asdict()
        #timestamp_index = rowDict["Index"]

        ts_dict = {}
        dict_multiassign(
            ts_dict,
            ["symbol", "date", "open", "high", "low", "close", "volume"],
            [
                symbol,
                rowDict["Index"],
                rowDict["_1"],
                rowDict["_2"],
                rowDict["_3"],
                rowDict["_4"],
                rowDict["_5"],
            ],
        )


        data.append(ts_dict)


        with backtest_db.atomic():
            query = Timeseries.insert_many(data)
            print(query)
            query.execute()
   