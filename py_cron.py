import sys
from datetime import datetime
import time
import subprocess

if len(sys.argv) != 3:
    print("python3 script.py file to execute the programm seconds.minutes.hours.days.months.years.days_of_the_week")
to_execute = sys.argv[1]
units_l = sys.argv[2].split(".")

seconds_l = []
minutes_l = []
hours_l = []
days_l = []
months_l = []
years_l = []
days_week_l = []

all_l_names = ["seconds", "minutes", "hours", "days", "months", "years", "days of the week"]
all_l = [seconds_l, minutes_l, hours_l, days_l, months_l, years_l, days_week_l]
units_limits = [60, 60, 24, 31, 12, "no", 7]

def leap_year(year):
        if not year:
            return False
        elif not year % 4:
            if not year % 100:
                if not year % 400:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

for I in range(0, len(all_l)):
    if "/" in units_l[I]:
        if units_limits[I] != "no":
            strt = units_l[I].split("/")
            cnt = int(strt[1])
            strt = int(strt[0])
            if strt + cnt > 7:
                print(f"The first jump goes outsite the limits of this time unit, which is '{all_l_names[I]}'")
                sys.exit()
            for i in range(strt, units_limits[I] + 1, cnt):
                all_l[I].append(i)
        else:
            print("No jump allowed for year")
            sys.exit()
    elif "-" in units_l[I]:
        strt = units_l[I].split("-")
        end = int(strt[1])
        strt = int(strt[0])
        if end < strt:
            print(f"End value of '{all_l_names[I]}' is lower than the start value")
            sys.exit()
        for i in range(strt, end, 1):
            all_l[I].append(i)
    elif units_l[I] != "*":
        all_l[I].append(int(units_l[I]))
    else:
        all_l[I].append("*")

animation = "|/-\\"
cnt = 0
print(sys.argv[1])

while 1:
    exec_status = False
    while not exec_status:
        time.sleep(1)
        cur_date = datetime.now()
        exec_status = True
        if int(cur_date.strftime("%Y")) not in years_l and years_l[0] != "*":
            exec_status = False
        if int(cur_date.strftime("%M")) not in months_l and months_l[0] != "*":
            exec_status = False
        if int(cur_date.strftime("%d")) not in days_l and days_l[0] != "*":
            exec_status = False
        if int(cur_date.weekday()) not in days_week_l and days_week_l[0] != "*":
            exec_status = False
        if int(cur_date.strftime("%H")) not in hours_l and hours_l[0] != "*":
            exec_status = False
        if int(cur_date.strftime("%M")) not in minutes_l and minutes_l[0] != "*":
            exec_status = False
        if int(cur_date.strftime("%S")) not in seconds_l and seconds_l[0] != "*":
            exec_status = False
        print(f"{int(cur_date.strftime('%S'))}:{int(cur_date.strftime('%M'))}:{int(cur_date.strftime('%H'))} {cur_date.strftime('%d')}/{cur_date.strftime('%M')}/{int(cur_date.strftime('%Y'))}", animation[cnt], end = "\r")
        if cnt < len(animation) - 1:
            cnt += 1
        else:
            cnt = 0
    subprocess.run(f"bash {sys.argv[1]}", shell = True, executable="/bin/bash")
    print("done")



