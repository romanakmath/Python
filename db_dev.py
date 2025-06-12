from database.db import backtest_db, Timeseries
import datetime

'''

backtest_db.connect()

Timeseries.drop_table()

Timeseries.create_table()

backtest_db.close()

'''

backtest_db.connect()

all_data = Timeseries.select()

for data in all_data:
    print({data.symbol})



Timeseries_data = [{"symbol": "A" }]

for t_data in Timeseries_data:
    print(t_data)
 #db_table = Timeseries_data.create(**t_data)

backtest_db.close()

