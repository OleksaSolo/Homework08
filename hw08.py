import collections
from collections import defaultdict
from datetime import datetime, timedelta

Users = collections.namedtuple("Users", ["name", "birthday"])

def get_birthdays_per_week(users):
    list_users_birthday_week = []
    today = datetime.now()
    print(f"Today {today.strftime('%A %d %B %Y')}")
    dtNow = today.date()
    now_weekday = today.weekday()
    end_day = dtNow+timedelta(weeks=1, days=5-now_weekday)
    start_day = end_day-timedelta(weeks=1)
    name_day = ['Monday: ', 'Tuesday: ', 'Wednesday:', 'Thursday:', 'Friday:']
    for i in users:
        dtCompare = str(dtNow.year) + str(users[i])[4:]
        birthday_user = datetime.strptime(dtCompare, '%Y-%m-%d')
        dtBDuser = birthday_user.date()
        if dtBDuser >= start_day and dtBDuser < end_day:
            line = (dtBDuser.weekday(), i)
            list_users_birthday_week.append(line)
    list_users_birthday_week.sort(key=lambda a: a[1])
    d = defaultdict(list)
    for day, name in list_users_birthday_week:
        d[day].append(name)
    for i in range(len(list_users_birthday_week)):
        if d[i] != []:
            print(name_day[i], ', '.join(d[i]))
    return "Don't forget to say happy birthday"

users1 = {"Bill":"1973-06-26", "Jill":"1986-06-26", 
          "Jack":"1983-06-29", "Jannet":"1992-06-27", 
          "Bill2":"1973-05-26", "Jill3":"1993-07-01", 
          "Jack1":"1973-06-30", "Jannet4":"1976-06-25"}
print(get_birthdays_per_week(users1))

