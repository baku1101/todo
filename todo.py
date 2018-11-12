#!/usr/bin/env python3
# -*- coding: utf8 -*-
import pickle
import datetime
import add_new_task
import argparse
import os
import sys

def find_top_priority_task():
    if (not os.path.exists(add_new_task.SAVEFILE)) or (add_new_task.load() == []):
        print('タスクがありません！新しく登録する時はadd_new_taskを実行してください。')
        sys.exit()
    data_list = add_new_task.load()
    top_task = data_list[0]
    for data_dict in data_list:
        if top_task['datetime'] > data_dict['datetime']:
            top_task = data_dict
    print('タスクは {0} ,期限は {1} です。'.format(top_task['name'],top_task['datetime']))
    return top_task

def set_timer(task):
    if os.uname()[1] in ['iPhone','iPad']:
        import timer_foriOS
        time = timer_foriOS.get_time()
        timer_foriOS.countup_timer(time)
    else:
        import timer_forPC
        time = input('時間のセット(hms): ')
        name = task['name']
        timer_forPC.App(time,name)

def remove_task(task):
    data_list = add_new_task.load()
    data_list.remove(task)
    add_new_task.save(data_list)

def parse():
    parser = argparse.ArgumentParser(description = 'This script will manage your task.')
    parser.add_argument('-s','--show-tasks',dest='show',action='store_true',default=False,help='show all tasks if this flag is set (default: False)')
    return parser.parse_args()

def show():
    data_list = add_new_task.load()
    print('現在のタスク数: {}'.format(len(data_list)))
    for data_dict in data_list:
        print('name: {0}, limit: {1}'.format(data_dict['name'],data_dict['datetime']))
    sys.exit()


if __name__ == '__main__':
    option = parse()
    if option.show:
        show()
    while True:
        top_task = find_top_priority_task()
        set_timer(top_task)
        remove_task(top_task)
        if input('新しいタスクを登録しますか? y/n : ') == 'y':
            add_new_task.add_new_task()
        else:
            pass
