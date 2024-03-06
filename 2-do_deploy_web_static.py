#!/usr/bin/python3
"""distruibutes an archive to my web servers"""
from fabric.api import env, put, run, local
from datetime import datetime
import os


env.hosts = ['54.196.29.133', '18.234.249.10']
env.user = 'ubuntu'

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


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split('/')[1]
        no_ext = file_name.split('.')[0]
        put(archive_path, "/tmp/{}".format(file_name))
        run("sudo mkdir -p /data/web_static/releases/{}/".format(no_ext))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, no_ext))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(no_ext, no_ext))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
