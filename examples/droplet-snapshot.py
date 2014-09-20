#!/usr/bin/env python
# encoding: utf-8

import pyocean
import time
import os

ACCESS_TOKEN = '' or os.getenv('ACCESS_TOKEN')
DROPLET_ID = '' or os.getenv('DROPLET_ID')

try:
    digitalocean = pyocean.DigitalOcean(ACCESS_TOKEN)
    droplet = digitalocean.droplet.get(DROPLET_ID)
    # Power off the droplet
    print("Turning off droplet '%s'." % droplet.name)
    droplet.power_off()
    # Create a snapshot
    image_name = 'snapshot_1'
    print("Creating snapshot '%s'. Please wait..." % image_name)
    droplet.snapshot(image_name)
    # Restore image. This will also power on the droplet.
    print("Restoring snapshot '%s'. Please wait..." % image_name)
    droplet.restore(image_name)
    print('done.')
except pyocean.exceptions.DOException as e:
    print(e)
