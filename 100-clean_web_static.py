#!/usr/bin/python3
""" Function that deletes outdated archives """
from fabric.api import *


env.hosts = ["34.202.158.130", "100.25.158.166"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    cleans up outdated archives
    """

    number = int(number)

    if number == 0:
        nums = 1
    else:
        nums = number

    local('cd versions ; ls -t | head -n -{} | xargs rm -rf'.format(nums))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | head -n -{} | xargs rm -rf'.format(path, nums))
