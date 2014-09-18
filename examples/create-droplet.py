#!/usr/bin/env python
# encoding: utf-8

"""
Create new droplet and list all droplets.
"""

import pyocean
import os
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
import pyocean

# Put your DigitalOcean access token here or get from environment variables
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

def main():
    try:
        digitalocean = pyocean.DigitalOcean(ACCESS_TOKEN)
        attrs = {
            'name': 'test-droplet-1',
            'region': 'nyc2',
            'size': '512mb',
            'image': 'ubuntu1204'
        }
        droplet = digitalocean.droplet.create(attrs)
        for droplet in digitalocean.droplet.all():
            print(droplet.name)
    except pyocean.exceptions.PyoceanException as e:
        print('ERROR: %s' % e)

if __name__ == "__main__":
    main()
