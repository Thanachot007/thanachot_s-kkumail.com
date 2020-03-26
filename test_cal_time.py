import time
start_hour = 13
start_minute = 30
year, month, day, hour, minute = time.strftime("%Y %m %d %H %M").split()
if int(minute) - int(start_minute) >= 15:
    print("late")
else:
    print("not late")
