import datetime
from datetime import datetime

def get_days_from_today():
    try:
        user_input = input("Введіть дату в форматі РРРР.ММ.ДД: ")
        user_date = datetime.strptime(user_input, "%Y.%m.%d")  #strptimetry:
        curent_date = datetime.today()
        print (((user_date - curent_date).days)+1)
    except Exception:
        print("Введена дата не відповідає формату РРРР.ММ.ДД")
        

get_days_from_today()
