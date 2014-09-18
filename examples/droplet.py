#!/usr/bin/env python
# encoding: utf-8

import pyocean
import os
import sys

"""
Create new droplet and list all droplets.
"""

# Put your DigitalOcean access token here or get from environment variables
ACCESS_TOKEN = '' or os.getenv('ACCESS_TOKEN')

def main():
    try:
        digitalocean = pyocean.DigitalOcean(ACCESS_TOKEN)
        # Create new droplet
        attrs = {
            'name': 'test_droplet_1',
            'region': 'nyc2',
            'size': '512mb',
            'image': 'ubuntu1204'
        }
        droplet = digitalocean.droplet.create(attrs=attrs)
        # List all droplets
        for droplet in digitalocean.droplet.all():
            print(droplet.name)
    except pyocean.exceptions.AuthException:
        print('Authentication failed.')
    except pyocean.exceptions.ApiException as e:
        print(e)

if __name__ == "__main__":
    main()
