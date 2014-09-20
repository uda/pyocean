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
    res = droplet.create_snapshot(image_name)
    print(res)
    # Restore image
    #print("Restoring snapshot. Please wait...")
    #droplet.restore_image(6204389)
    print('done.')
except pyocean.exceptions.DOException as e:
    print(e)
