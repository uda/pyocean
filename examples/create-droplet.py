#!/usr/bin/env python
# encoding: utf-8

"""
Create new droplet and list all droplets.
"""

from os.path import dirname, abspath
import os
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
import pyocean

# Put your DigitalOcean access token here or set from environment variables
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', '')

try:
    digitalocean = pyocean.DigitalOcean(ACCESS_TOKEN)
    attrs = {
        'name': 'test-droplet-1',
        'region': 'nyc2',
        'size': '512mb',
        'image': 'fedora-19-x32'
    }
    droplet = digitalocean.droplet.create(attrs)
    for droplet in digitalocean.droplet.all():
        print(droplet)
except pyocean.exceptions.DOException as e:
    print('ERROR %s: %s' % (e.code, e.message))

