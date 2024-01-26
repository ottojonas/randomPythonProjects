#Has a funky way of showing the time after the day is over, but it works

import datetime
import time

def countdown(d, h, m, s):

    idk = d * 86400 + h * 3600 + m * 60 + s
    while idk > 0:
        timer = datetime.timedelta(seconds = idk) 
        mins, secs = divmod(idk, 60) 
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        print(timer, end="\r")
        time.sleep(1)
        idk -= 1

    print('timer complete')

d = input("Enter the number of days: ")
h = input("Enter the number of hours: ")
m = input("Enter the number of minutes: ") 
s = input("Enter the number of seconds: ")

countdown(int(d), int(h), int(m), int(s))