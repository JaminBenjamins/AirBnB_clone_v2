#!/usr/bin/python3

import os
from fabric.api import env, put, run

env.hosts = ['100.26.159.112', '54.237.126.53']


def do_deploy(archive_path):
    """
        Deploys the static files to the host server
            Args:
                archive_path(str): The path of archive to distribute.
            Returns:
                True if all operations have been done correctly
                Otherwise return False
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print("New version deployed!")
        success = True
    except Exception:
        success = False
    return success
