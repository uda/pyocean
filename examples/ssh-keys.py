#!/usr/bin/env python
# encoding: utf-8

"""
Add new SSH key, list all keys, and delete the previously created key.
"""

import pyocean
import os

# Put your DigitalOcean access token here or set from environment variables
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', '')

try:
    digitalocean = pyocean.DigitalOcean(ACCESS_TOKEN)
    # Create new key
    key = digitalocean.ssh_key.create({
        'name': 'sample SSH key',
        'public_key': open('/path/to/id_rsa.pub').read()
    })
    # List all SSH keys
    for item in digitalocean.ssh_key.all():
        print(item)
    # Delete the previously created key
    key.delete()
except pyocean.exceptions.DOException as e:
    print(e)
