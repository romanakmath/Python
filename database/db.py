import peewee
from playhouse.sqlite_ext import SqliteExtDatabase


backtest_db = SqliteExtDatabase(
    "backtest.db",
    pragmas={
        "journal_mode": "wal",  # WAL-mode.
        "cache_size": -64 * 1000,  # 64MB cache.
        "synchronous": 0,
    },
)  # Let the OS manage syncing.




class Timeseries(peewee.Model):
    symbol = peewee.CharField()
    date = peewee.DateTimeField()
    open = peewee.FloatField()
    high = peewee.FloatField()
    low = peewee.FloatField()
    close = peewee.FloatField()
    volume = peewee.FloatField()


    class Meta:
        database = backtest_db
        db_table = "crypto_tseries"
        primary_key = peewee.CompositeKey("symbol", "date")




# Recreate the table if it exists
Timeseries.drop_table()
Timeseries.create_table()
