#!/usr/bin/env python3
# -*- coding: utf8 -*-

import dropbox

dbx = dropbox.Dropbox('1VBymHjFksAAAAAAAAARVCi7nHzqp42BATYy8TdB2cdNtuGqRrJjCujwApWFTyE1')

def save():
    with open('./todo.save', 'rb') as f:
        dbx.files_upload(f.read(), '/todo/todo.save',mode=dropbox.files.WriteMode.overwrite)

def load():
    with open('./todo.save', 'wb') as f:
        metadata, res = dbx.files_download('/todo/todo.save')
        f.write(res.content)
