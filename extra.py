import time
from datetime import datetime
import os, sys
from pathlib import Path
from random import choice
import json
import socket

log = print

def print(*args):
    log(f"INFO [{datetime.now().strftime('%d-%m-%Y  %H:%M:%S')}] { ' '.join(args)}")


def resource_path(relative_path):
    path=os.path.dirname(sys.executable)    
    return path+'/'+relative_path

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def timeCal(sec):
    if sec < 60:
        return f"{sec} Sec"
    elif sec < 3600:
        return f"{sec//60}:{ str(sec%60)[:2]} Mint"
    elif sec < 216000:
        return f"{sec//3600}:{ str(sec%3600)[:2]} Hrs"
    elif sec < 12960000:
        return f"{sec//216000}:{ str(sec%216000)[:2]} Days"
    else:
        return "CE"
    
    
    
def data_size_cal(size):
    st=None
    if size < 1024:
        st=f'{size} Bytes'
        
    elif size < 1022976 :
        size=str(size/1024).split('.')
        size=size[0]+'.'+(size[1])[:1]
        st=f'{size} KB'

    elif size < 1048576 :
        size=str(size/1048576).split('.')
        size=size[0]+'.'+(size[1])[:2]
        st=f'{size} MB'

    elif size < 1047527424:
        
        size=str(size/1048576).split('.')
        size=size[0]+'.'+(size[1])[:1]
        st=f'{size} MB'
        
    elif size < 1073741824:
        
        size=str(size/1073741824).split('.')
        size=size[0]+'.'+(size[1])[:2]
        st=f'{size} GB'
        
    elif size >= 1073741824:
        size=str(size/1073741824).split('.')
        size=size[0]+'.'+(size[1])[:1]
        st=f'{size} GB'
    else:
        st='Error_in_cal'
    return st


def genSessionId(len_ = 50, idList= []):
    data = "zxcvbnmasdfghjklqwertyuiop1234567890@ZXCVBNMASDFGHJKLQWERTYUIOP&&&&"
    id_ = ""
    for i in range(len_):
        id_ += choice(data)
    
    if id_ in idList:
        genSessionId(len_, idList)
    else:
        return id_
    

class DataBabse(dict):
    def __init__(self) -> None:

        self.file_name = "data/db.tube"
        self.path = resource_path(self.file_name)
        self.load()


    def read(self):
        with open(self.path, "r") as ff:
            try:
                return json.loads(ff.read())
            except:
                print("Invalid Json")
                self.init_schema()


    def load(self):
        self.update(self.read())

    def write(self, data):
        with open(self.path, "w") as tf:
            tf.write(json.dumps(data))

    def commit(self):
        self.write(self)

    def init_schema(self):
        self.schema = {
            "downloads" : [], # downloaded files
        }

        self.write(self.schema)
        self.load()


def isOnline(self):
    try:
        s  = socket.socket()
        s.settimeout(0.5)
        s.connect(("pythonanywhere.com",443))
        s.close()
        return True
    except:
        return False
    