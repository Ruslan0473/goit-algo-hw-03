import datetime as dt
from datetime import datetime as dtdt
users = [
    {"name": "John Do", "birthday": "1985.02.02"},
    {"name": "Ane Smith", "birthday": "1990.02.01"},
    {"name": "Ohn De", "birthday": "1985.02.04"},
    {"name": "Jane Sith", "birthday": "1990.02.03"}
]


def get_upcoming_birthdays(users=None):
    today_date=dtdt.today().date()
    congratulation_date=[]
    for user in users:
        birth_date=user["birthday"]
        birth_date=str(today_date.year)+birth_date[4:]
        birth_date=dtdt.strptime(birth_date, "%Y.%m.%d").date()
        week_day=birth_date.isoweekday()
        days_between=(birth_date-today_date).days
        if 0<=days_between<7:
            if week_day<6:
                congratulation_date.append({'birthday':birth_date.strftime("%Y.%m.%d"), 'name':user['name']})
            else:
                if (birth_date+dt.timedelta(days=1)).weekday()==0:
                    congratulation_date.append({'name':user['name'], 'birthday':(birth_date+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (birth_date+dt.timedelta(days=2)).weekday()==0:
                    congratulation_date.append({'name':user['name'], 'birthday':(birth_date+dt.timedelta(days=2)).strftime("%Y.%m.%d")})

    return congratulation_date

print(get_upcoming_birthdays(users))