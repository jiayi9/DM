
import datetime
from datetime import timedelta

def find_starting_time(now, input_type = "builtin", output_type = "builtin", FORMAT = '%Y-%m-%d %H:%M:%S'):
    if input_type == "string":
        now = datetime.datetime.strptime(now, FORMAT)
    HOUR = now.hour
    YEAR = now.year
    MONTH = now.month
    DAY = now.day
    SHIFT_HOURS_MORNING = [7,8,9,10,11,12,13,14]
    SHIFT_HOURS_DAY = [15,16,17,18,19,20,21,22]
    SHIFT_HOURS_NIGHT = [23,0,1,2,3,4,5,6]
    if HOUR in SHIFT_HOURS_MORNING:
        print("Morning")
        REF = datetime.datetime(YEAR, MONTH, DAY, 7,0,0)
    elif HOUR in SHIFT_HOURS_DAY:
        print("Day")
        REF = datetime.datetime(YEAR, MONTH, DAY, 15,0,0)
    elif HOUR in SHIFT_HOURS_NIGHT:
        print("Night")
        if HOUR == 23:
            REF = datetime.datetime(YEAR, MONTH, DAY, 23,0,0)
        else:
            REF = datetime.datetime(YEAR, MONTH, DAY, 23,0,0) - timedelta(days = 1)
    else:
        print("Hour error")
    if output_type == "string":
        return(REF.strftime(FORMAT))
    else:
        return(REF)    
