#!/usr/bin/env python3
# -*- coding: utf8 -*-
import pickle
import os
import datetime
import sys
if (not os.uname()[1] in ['iPhone','iPad']):
    import readline
else:
    import save_sync

ACHIEVEFILE = ''

def set_achievefile_env():
    if os.environ.get('TODOACHIEVE') == None:
        print('環境変数"TODOACHIEVE"を設定してください\n(相対パスだと動かない?)')
        sys.exit(1)
    else:
        global ACHIEVEFILE
        ACHIEVEFILE = os.environ.get('TODOACHIEVE') + 'todo.achieve'

def save(data_list):
    global ACHIEVEFILE
    with open(ACHIEVEFILE, 'wb') as achievefile:
        pickle.dump(data_list,achievefile)

def load():
    global ACHIEVEFILE
    if os.path.isfile(ACHIEVEFILE):
        with open(ACHIEVEFILE, 'rb') as achievefile:
            data_list = pickle.load(achievefile)
            return data_list
    else:
        save([])
        return []

def add_achieve(achieve):
    set_achievefile_env()
    dt = datetime.date.today()
    data_dict = {'name':achieve,'date':dt}
    data_list = []
    data_list = load()
    data_list.append(data_dict)
    save(data_list)

if __name__ == '__main__':
    if (os.uname()[1] in ['iPhone','iPad']):
        save_sync.load()
        os.environ['TODOACHIEVE'] = '/private/var/mobile/Containers/Shared/AppGroup/BD1DA245-5619-467F-B9B5-34FF6EFCCDE2/Pythonista3/Documents/todo/'
    set_achievefile_env()
