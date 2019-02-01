#!/usr/bin/env python3
# -*- coding: utf8 -*-
import pickle
import datetime
import argparse
import os
import sys

import add_new_task
import add_achieve

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
        str_time = timer_foriOS.get_time()
        time = timer_foriOS.anal_str_time(str_time)
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
    parser.add_argument('-a','--show-achieves',dest='achieves',action='store_true',default=False,help='show all achieves if this flag is set (default: False)')
    return parser.parse_args()

def show_tasks():
    data_list = add_new_task.load()
    print('現在のタスク数: {}'.format(len(data_list)))
    for data_dict in data_list:
        print('name: {0}, limit: {1}'.format(data_dict['name'],data_dict['datetime']))
    sys.exit()

def show_achieves():
    data_list = add_achieve.load()
    print('達成した項目数: {}'.format(len(data_list)))
    for data_dict in data_list:
        print('name: {0}, date: {1}'.format(data_dict['name'],data_dict['date']))
    sys.exit()

def set_environ_foriOS():
    os.environ['TODOSAVE'] = '/private/var/mobile/Containers/Shared/AppGroup/BD1DA245-5619-467F-B9B5-34FF6EFCCDE2/Pythonista3/Documents/todo/'
    os.environ['TODOACHIEVE'] = '/private/var/mobile/Containers/Shared/AppGroup/BD1DA245-5619-467F-B9B5-34FF6EFCCDE2/Pythonista3/Documents/todo/'

if __name__ == '__main__':
    if (os.uname()[1] in ['iPhone','iPad']):
        import save_sync
        savefiles_on_dropbox = ['/todo/todo.save','/todo/todo.achieve']
        savefiles_on_device = ['./todo.save','./todo.achieve']
        save_sync.load(savefile_on_device,savefile_on_dropbox)
        set_environ_foriOS()
    add_new_task.set_savefile_env()
    add_achieve.set_achievefile_env()
    option = parse()
    if option.show:
        show_tasks()
    if option.achieves:
        show_achieves()
    while True:
        top_task = find_top_priority_task()
        set_timer(top_task)
        remove_task(top_task)
        if (os.uname()[1] in ['iPhone','iPad']):
            savefile_on_dropbox = '/todo/todo.save'
            savefile_on_device = './todo.save'
            save_sync.save(savefile_on_device,savefile_on_dropbox)
        if input('新しいタスクを登録しますか? y/n : ') == 'y':
            add_new_task.add_new_task()
        if input('タスクを達成したリストに登録しますか? y/n : ') == 'y':
            achieve_task = input('達成した項目を入力 : ')
            add_achieve.add_achieve(achieve_task)
