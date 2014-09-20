#!/usr/bin/env python
# encoding: utf-8

"""
Reboot a droplet.
"""

import pyocean
import time
import os

# Put your DigitalOcean access token here or set from environment variables
ACCESS_TOKEN = '' or os.getenv('ACCESS_TOKEN')
DROPLET_ID = '' or os.getenv('DROPLET_ID')

try:
    digitalocean = pyocean.DigitalOcean(ACCESS_TOKEN)
    droplet = digitalocean.droplet.get(DROPLET_ID)
    print("Rebooting droplet '%s'..." % droplet.name)
    droplet.reboot()
except pyocean.exceptions.DOException as e:
    print('Reboot failed: %s' % e)
else:
    print('done.')
