import collections
from collections import defaultdict
from datetime import datetime, timedelta

Users = collections.namedtuple("Users", ["name", "birthday"])

def get_birthdays_per_week(users):
    list_users_birthday_week = []
    today = datetime.now()
    print(f"\nToday {today.strftime('%A %d %B %Y')}")
    print("\nBirthdays next week:\n")
    dtNow = today.date()
    now_weekday = today.weekday()
    end_day = dtNow+timedelta(weeks=1, days=5-now_weekday)
    start_day = end_day-timedelta(weeks=1)
    name_day = ['Monday: ', 'Tuesday: ', 'Wednesday:', 'Thursday:', 'Friday:']
    #print(start_day, " : ", end_day)
    for i in users:
        dtCompare = str(dtNow.year) + str(users[i])[4:]
        birthday_user = datetime.strptime(dtCompare, '%Y-%m-%d')
        dtBDuser = birthday_user.date()
        #print(f"dtBDuser = {dtBDuser}")
        if dtBDuser >= start_day and dtBDuser < end_day:
            if dtBDuser.weekday() == 5 or dtBDuser.weekday() == 6:
                num_day = 0
            else:
                num_day = dtBDuser.weekday()
            line = (num_day, i)
            #print(line)
            list_users_birthday_week.append(line)
    list_users_birthday_week.sort(key=lambda a: a[1])
    d = defaultdict(list)
    for day, name in list_users_birthday_week:
        d[day].append(name)
    # print("d =", d)
    # print(len(d))
    # for j in range(len(name_day)):
    #     if d[j] != []:
    #         print(name_day[j], d[j])
    for j in range(len(list_users_birthday_week)):
    #for j in range(len(d)):
        #print(j, name_day[j], name[j], d[j])
        if d[j] != []:
            print(name_day[j], ', '.join(d[j]))
    return "\nDon't forget to say happy birthday!\n"

users1 = {"Bill":"1973-06-26", "Jill":"1986-06-26", 
          "Jack":"1983-06-29", "Jannet":"1992-06-27", 
          "Bill2":"1973-07-02", "Jill3":"1993-07-01", 
          "Jack1":"1973-06-30", "Jannet4":"1976-07-05"}
print(get_birthdays_per_week(users1))

