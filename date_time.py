import time
import datetime
import locale
import pytz

# print(time.time())
# print(time.localtime())
def aktuelle_uhrzeit():
    aktuelle_zeit = time.localtime()
    formatierte_zeit = time.strftime("%H:%M:%S", aktuelle_zeit)
    print(f"Die aktuelle Uhrzeit ist {formatierte_zeit}")
    aktuelle_datum = datetime.datetime.now()
    print(aktuelle_datum)
    formatiertes_datum = aktuelle_datum.strftime("%A %d. %B %Y %H:%M:%S.%f")
    print(f"Das aktuelle Datum ist {formatiertes_datum}")
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    microsecond = datetime.datetime.now().microsecond
    print(f"{year} {month} {day} {hour} {minute} {second} {microsecond}")
    print(f"Isoformat: {datetime.datetime.now().isoformat()}")
    locale.setlocale(locale.LC_ALL, 'german')    
    print(datetime.datetime.now().strftime('%A, %d. %B %Y'))
    today = datetime.date.today()
    print(today)
    utc = datetime.datetime.now(pytz.utc)
    print(utc)
    localtime = utc.astimezone()
    print(localtime)

aktuelle_uhrzeit()