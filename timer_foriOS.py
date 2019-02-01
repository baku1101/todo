#!/usr/bin/env python3
# -*- coding: utf8 -*-

# for pythonista (iOS app)
from time import sleep
import os
import sys
import re
import notification

def get_time():
    str_time = input('時間設定(hms):')
    return str_time

def anal_str_time(str_time):
    if re.search("\A(?:\d+h)?(?:\d+m)?(?:\d+s)?$", str_time) is None:
        print("Incorrect format of period:", str_time)
        print("Set period like 10m30s")
        sys.exit()
    time = 0
    if re.search("\d+h", str_time) is not None:
        time += int(re.search("\d+h", str_time).group(0)[:-1]) * 3600
    if re.search("\d+m", str_time) is not None:
        time += int(re.search("\d+m", str_time).group(0)[:-1]) * 60
    if re.search("\d+s", str_time) is not None:
        time += int(re.search("\d+s", str_time).group(0)[:-1])
    if time > 9 * 3600 + 59 * 60 + 59:
        print("Too long period.")
        sys.exit()
    return time

def countup_timer(time):
    for past in range(0,time):
        if((time - past) % 600 == 0):
            notification.schedule('todo:残り{}分'.format((time - past)//60),past,'arcade:Coin_2')
    notification.schedule('todo:終了です',time,'arcade:Coin_1')
    print()

if __name__ == '__main__':
    str_time = get_time()
    time = anal_str_time(str_time)
    countup_timer(time)
