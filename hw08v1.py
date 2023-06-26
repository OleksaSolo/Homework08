import collections
from datetime import datetime, timedelta

Users = collections.namedtuple("Users", ["name", "birthday"])

def get_birthdays_per_week(users):
    day_weeks = {}
    list_users_birthday_week = []
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    today = datetime.now()
    print(f"Today {today.strftime('%A %d %B %Y')}")
    print("\nDon't forget to say happy birthday next week:")
    dtNow = today.date()
    now_weekday = today.weekday()
    end_day = dtNow+timedelta(weeks=1, days=5-now_weekday)
    start_day = end_day-timedelta(weeks=1)
    for i in users:
        dtCompare = str(dtNow.year) + str(users[i])[4:]
        birthday_user = datetime.strptime(dtCompare, '%Y-%m-%d')
        dtBDuser = birthday_user.date()
        if dtBDuser >= start_day and dtBDuser < end_day:
            line = (i, dtBDuser.weekday())
            list_users_birthday_week.append(line)
    list_users_birthday_week.sort(key=lambda a: a[1])
    for item in list_users_birthday_week:
        day_week = item[1]
        if day_week == 5 or day_week == 6 or day_week == 0:
            #day_weeks["Monday"] = item[0]
            monday.append(item[0])
        elif day_week == 1:
            #day_weeks["Tuesday"] = item[0]
            tuesday.append(item[0])
        elif day_week == 2:
            wednesday.append(item[0])
        elif day_week == 3:
            thursday.append(item[0])
        elif day_week == 4:
            friday.append(item[0])
    #print(len(day_weeks))
    #print("day_weeks = " , day_weeks)
    out = ''
    if len(monday) > 0:
        out += "\nMonday: "
        for i in monday:
            out += i + ', '
        out = out.removesuffix(', ')
    if len(tuesday) > 0:
        out += "\nTuesday: "
        for i in tuesday:
            out += i + ', '
        out = out.removesuffix(', ')
    if len(wednesday) > 0:
        out += "\nWednesday: "
        for i in wednesday:
            out += i + ', '
        out = out.removesuffix(', ')
    if len(thursday) > 0:
        out += "\nThursday: "
        for i in thursday:
            out += i + ', '
        out = out.removesuffix(', ')
    if len(friday) > 0:
        out += "\nFriday: "
        for i in friday:
            out += i + ', '
        out = out.removesuffix(', ')
    return out
    

users1 = {"Bill":"1973-06-26", "Jill":"1976-06-26", 
          "Jack":"1973-06-29", "Jannet":"1976-06-27", 
          "Bill2":"1973-07-02", "Jill3":"1976-07-01", 
          "Jack1":"1973-06-30", "Jannet4":"1976-07-05"}
print(get_birthdays_per_week(users1))


'''
Имеется json:

{'city':'Moscow', 'manager':'Igor'},
{'city':'Kazan', 'manager':'Valera'},
{'city':'Moscow', 'manager':'Olga'},
{'city':'Kazan', 'manager':'Natalia'},
{'city':'Moscow', 'manager':'Oleg'},


Как легко и грамотно сделать такую структуру?

'Moscow': ['Igor','Olga','Oleg'],
'Kazan': ['Valera','Natalia']


Ответ:

res = {}
for d in ({'city': 'Moscow', 'manager': 'Igor'},
          {'city': 'Kazan', 'manager': 'Valera'},
          {'city': 'Moscow', 'manager': 'Olga'},
          {'city': 'Kazan', 'manager': 'Natalia'},
          {'city': 'Moscow', 'manager': 'Oleg'}):
    res.setdefault(d['city'], []).append(d['manager'])
print(res)

'''