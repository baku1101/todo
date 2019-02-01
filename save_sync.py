#!/usr/bin/env python3
# -*- coding: utf8 -*-

# dropboxにあるセーブファイルに対してsave,loadするためのスクリプト
# for iOS
# Dropbox//アプリ/db_pythonista_synchronator/todo以下に保存するようになっている

import dropbox

dbx = dropbox.Dropbox('1VBymHjFksAAAAAAAAARVCi7nHzqp42BATYy8TdB2cdNtuGqRrJjCujwApWFTyE1')

def save(savefiles_on_device,savefiles_on_dropbox):
    for index in range(0,len(savefiles_on_dropbox)):
        with open(savefiles_on_device[index], 'rb') as f:
            dbx.files_upload(f.read(), savefiles_on_dropbox[index],mode=dropbox.files.WriteMode.overwrite)

def load(savefiles_on_device,savefiles_on_dropbox):
    for index in range(0,len(savefiles_on_dropbox)):
        with open(savefiles_on_device[index], 'wb') as f:
            metadata, res = dbx.files_download(savefiles_on_dropbox[index])
            f.write(res.content)

if __name__ == '__main__':
    load()

