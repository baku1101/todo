#!/usr/bin/env python3
# -*- coding: utf8 -*-

import dropbox

dbx = dropbox.Dropbox('1VBymHjFksAAAAAAAAARVCi7nHzqp42BATYy8TdB2cdNtuGqRrJjCujwApWFTyE1')

savefile_on_dropbox = '/todo/todo.save'
savefile_on_device = './todo.save'
def save():
    with open(savefile_on_device, 'rb') as f:
        dbx.files_upload(f.read(), savefile_on_dropbox,mode=dropbox.files.WriteMode.overwrite)

def load():
    with open(savefile_on_device, 'wb') as f:
        metadata, res = dbx.files_download(savefile_on_dropbox)
        f.write(res.content)

if __name__ == '__main__':
    load()

