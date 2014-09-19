#!/usr/bin/env python
# encoding: utf-8

"""
List all of your droplets.
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
    for droplet in digitalocean.droplet.all():
        print('%s (%s)' % (droplet.name, droplet.image['name']))
except pyocean.exceptions.DOException as e:
    print('ERROR: %s' % e)
