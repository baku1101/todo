#!/usr/bin/env python3
# -*- coding: utf8 -*-
import pickle
import os
import datetime
import sys
if (not os.uname()[1] in ['iPhone','iPad']):
    import readline

SAVEFILE = ''

def set_savefile_env():
    if os.environ.get('TODOSAVE') == None:
        print('環境変数"TODOSAVE"を設定してください\n(相対パスだと動かない?)')
        sys.exit(1)
    else:
        global SAVEFILE
        SAVEFILE = os.environ.get('TODOSAVE') + 'todo.save'

def create_new_task():
    name = input('タスク名を入力: ')
    print('期限の入力↓')
    limit = {'year':0, 'month':0, 'date':0, 'hour':0}
    limit['year'] = int(input('year: '))
    limit['month'] = int(input('month: '))
    limit['date'] = int(input('date: '))
    limit['hour'] = int(input('hour: '))
    dt = datetime.datetime(limit['year'],limit['month'],limit['date'],limit['hour'])
    data_dict = {'name':name,'datetime':dt}
    return data_dict

def save(data_list):
    with open(SAVEFILE, 'wb') as savefile:
        pickle.dump(data_list,savefile)

def load():
    if os.path.isfile(SAVEFILE):
        with open(SAVEFILE, 'rb') as savefile:
            data_list = pickle.load(savefile)
            return data_list
    else:
        save([])
        return []

def add_new_task():
    data_dict = create_new_task()
    data_list = []
    data_list = load()
    data_list.append(data_dict)
    save(data_list)

if __name__ == '__main__':
    set_savefile_env()
    while True:
        add_new_task()
        if input('続けてタスクを登録しますか? y/n :') == 'n':
            sys.exit()
        else:
            pass
