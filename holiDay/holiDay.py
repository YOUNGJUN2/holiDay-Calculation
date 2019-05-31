from datetime import datetime, timedelta, date

def inputDay(month, day):
    month=int(month)
    day=int(day)
    i = 0

    designated_day = datetime(2019, month, day)
    day_off = datetime(2019, 3, 2)
    number_days = (designated_day-day_off).days
    day_off_L = []

    while(i<(number_days//4)):
        day_off = (day_off + timedelta(days=4))
        day_off_L.append(day_off)
        
        if datetime.date(day_off).weekday() == 5:
            day_off_L.append(day_off+timedelta(days=1))
        i+=1


    if designated_day in day_off_L:
        result = '쉬는 날!
        '
    else:
        result = '일하는 날!'
        
    return result

