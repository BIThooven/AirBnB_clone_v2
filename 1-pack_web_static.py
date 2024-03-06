#!/usr/bin/python3
"""a python file to compress web static into a tgz file"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """genrating a tgz archive"""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        print("web_static packed: {} -> {}Bytes".format(file_name,
              os.path.getsize(file_name)))
        return file_name
    except Exception:
        return None
