#!/usr/bin/env python3
# -*- coding: utf8 -*-
from time import sleep
import os
import sys

def get_time():
    time = int(input('何分でやる？ :'))
    return time

def countup_timer(time):
    for i in range(0,time * 60 + 1):
        minutes = i // 60
        seconds = i - minutes * 60
        print(' {0} 分 {1} 秒経過'.format(minutes,seconds))
        sleep(1)
    print('終了です')
