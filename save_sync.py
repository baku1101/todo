#!/usr/bin/env python3
# -*- coding: utf8 -*-

# dropboxにあるセーブファイルに対してsave,loadするためのスクリプト
# for iOS
# Dropbox//アプリ/db_pythonista_synchronator/todo以下に保存するようになっている

import dropbox

dbx = dropbox.Dropbox('1VBymHjFksAAAAAAAAARVCi7nHzqp42BATYy8TdB2cdNtuGqRrJjCujwApWFTyE1')

savefile_on_dropbox = '/todo/todo.save'
savefile_on_device = './todo.save' # for iOS
def save(savefile_on_device,savefile_on_dropbox):
    with open(savefile_on_device, 'rb') as f:
        dbx.files_upload(f.read(), savefile_on_dropbox,mode=dropbox.files.WriteMode.overwrite)

def load(savefile_on_device,savefile_on_dropbox):
    with open(savefile_on_device, 'wb') as f:
        metadata, res = dbx.files_download(savefile_on_dropbox)
        f.write(res.content)

if __name__ == '__main__':
    load()

