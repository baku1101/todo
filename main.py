#!/usr/bin/env python3
# -*- coding: utf8 -*-
import pickle
import datetime
import add_new_task
import os

def find_top_priority_task():
    if (not add_new_task.SAVEFILE in os.listdir('./')) or (add_new_task.load() == []):
        print('タスクがありません！新しく登録する時はadd_new_taskを実行してください。')
        add_new_task.add_new_task()
    data_list = add_new_task.load()
    top_task = data_list[0]
    for data_dict in data_list:
        if top_task['datetime'] > data_dict['datetime']:
            top_task = data_dict
    print('タスクは {0} ,期限は {1} です。'.format(top_task['name'],top_task['datetime']))
    return top_task

def set_timer(task):
    import os
    if os.uname()[1] in ['iPhone','iPad']:
        import timer_foriOS
        time = timer_foriOS.get_time()
        timer_foriOS.countup_timer(time)
    else:
        import timer_forPC
        time = input('時間のセット(hms): ')
        name = task['name']
        timer = timer_forPC.App(time,name)

def remove_task(task):
    data_list = add_new_task.load()
    data_list.remove(task)
    add_new_task.save(data_list)

if __name__ == '__main__':
    while True:
        top_task = find_top_priority_task()
        set_timer(top_task)
        remove_task(top_task)
        if input('新しいタスクを登録しますか? y/n : ') == 'y':
            add_new_task.add_new_task()
        else:
            pass
