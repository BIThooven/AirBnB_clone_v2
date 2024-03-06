#!/usr/bin/python3
"""distruibutes an archive to my web servers"""
from fabric.api import *
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
    file_name = archive_path.split('/')[1]
    file_path = '/data/web_static/releases/'
    releases_path = file_path + file_name[:-4]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, releases_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed!')
        return True
    except Exception:
        return False
