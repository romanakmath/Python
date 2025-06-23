from database.get_yfinance_data import get_yfinance_data
from datetime import datetime as dt
import yfinance as yf
import calendar
import sqlite3
import pytickersymbols as pyt
from database.db import backtest_db, Timeseries

from datetime import datetime, timedelta

from database.insert_db import ins_data

def add_days(n, d = datetime.today()):
  return d + timedelta(n)

# print('Enter start (yyyy-mm-dd):')
# start = input()

# print('Enter end (yyyy-mm-dd):')
# end = input()


check_start = "2024-08-06"
check_end =  "2024-08-21"
format_data = "%Y-%m-%d"

count_working_days = 0
start_search = 0

check_start_day = dt.strptime(check_start, format_data).date()
check_end_day = dt.strptime(check_end, format_data).date()

while start_search == 0:
    
    if check_start_day == check_end_day:
            start_search = 1
    weekday =calendar.day_name[check_start_day.weekday()]

    working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    if weekday in working_days:
         count_working_days += 1  

    check_start_day= add_days(1, check_start_day)

####### Deutschlandweite
####### Neujahr 01.01.
####### Karfreitag flexibel
####### Ostermontag flexibel
####### Christi Himmelfahrt flexibel
####### Pfingstmontag flexibel
####### 1. Mai
####### 03.10.
####### 24.12.
####### 25.12.
####### andere Feiertage + was ist mit 24.12. und 31.12.

#Check 7 Einträge pro Tag
sql = "SELECT date(tag), symbol, count(*) "\
      "FROM crypto_tseries t1 "\
      "where date(tag) <= date('"+ check_end +"') "\
      "and date(tag) >= date('" + check_start +"') "\
      "group by date(tag), symbol "\
      "having count(*) <> 7 "
cursor = backtest_db.cursor()
cursor.execute(sql)
cursor.fetchone()

for x in cursor:
    print(x)
cursor.close()

#Check 7 verschiede Einträge pro Tag
sql = "SELECT date(tag), symbol, count(distinct tag) "\
      "FROM crypto_tseries t1 "\
      "where date(tag) <= date('"+ check_end +"') "\
      "and date(tag) >= date('" + check_start +"') "\
      "group by date(tag), symbol "\
      "having count(distinct tag) <> 7 "
cursor = backtest_db.cursor()
cursor.execute(sql)
cursor.fetchone()

for x in cursor:
    print(x)
cursor.close()


##############
###offen Wochenende + Feiertage auslassen aus Prüfung
#############

#Check alle Tage da
sql = "SELECT  count(distinct(date(tag))), symbol "\
      "from crypto_tseries "\
      "where date(tag) <= date('"+ check_end +"') "\
      "and date(tag) >= date('" + check_start +"') "\
      "group by symbol "\
      "having count(distinct(date(tag))) <>  " + str(count_working_days)
cursor = backtest_db.cursor()
cursor.execute(sql)
cursor.fetchone()

for x in cursor:
    print(x)
cursor.close()

#Check mindestens ein Eintrag im Zeitraum da
# for ticker in ["MSFT", "AAPL", "DDDD"]:
#     sql1 = "SELECT count(*) "+\
#       "from crypto_tseries "+\
#       "where date(tag) <= date('"+ check_end +"') "+\
#       "and date(tag) >= date('" + check_start +"') "
#     sql2 = "and symbol = \"" + ticker + "\" "+\
#       "having count(*) = 0 "
#     sql = sql1 + sql2
#     cursor = backtest_db.cursor()
#     cursor.execute(sql)
#     cursor.fetchone()

#     for x in cursor:
#         print(ticker)
#     cursor.close()   


# for ticker in ["MSFT", "AAPL", "DDDD"]:
#     sql1 = "SELECT count(*) "+\
#       "from crypto_tseries "+\
#       "where date(tag) <= date('"+ check_end +"') "+\
#       "and date(tag) >= date('" + check_start +"') "
#     sql2 = " and symbol = ':sym'  "+\
#       "having count(*) = 0 "
for ticker in ["MSFT", "AAPL", "PSTS"]:

    sql1 = (
            "SELECT count(*) as Anz "
            + "from crypto_tseries "
            + "where date(tag) <= date('"
            + check_end
            + "') "
            + "and date(tag) >= date('"
            + check_start
            + "') "
            )
    sql2 = " and symbol = '" + ticker + "'  " + "having count(*) = 0 "
    sql = sql1 + sql2
 
    # param={'sym':ticker}
    cursor = backtest_db.cursor()
    cursor.execute(sql)

    for x in cursor:
        print("Fehler Daten in Zeitraum für Ticker nicht da: " + ticker)
    cursor.close


    temp = cursor.fetchone()

    # if temp is not None and temp[0] == 0:
    #        print("Fehler Daten in Zeitraum für Tock nicht da" + ticker)


 #"and symbol = %s "+\

# check_day= check_start
# do_loop = True

# while do_loop or check_end==check_day:
#     # Wochenende auschließen
#     # Was ist mit Feiertagen
#     print(check_day)

#     #Daten in Tabelle prüfen 

#     startdate = dt.strptime(check_day, format_data).date()
#     startdate= add_days(1, startdate)
#     check_day = dt.strftime(startdate, format_data)
    
#     if check_day == check_end:
#        do_loop = False 