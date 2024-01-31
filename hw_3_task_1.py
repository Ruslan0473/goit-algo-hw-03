import datetime
from datetime import datetime




def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, "%Y.%m.%d")  #strptimetry:
        curent_date = datetime.today()
        print (((user_date - curent_date).days)+1)
    except Exception:
        print("Введена дата не відповідає формату РРРР.ММ.ДД")


date = input("Введіть дату в форматі РРРР.ММ.ДД: ")
get_days_from_today(date)