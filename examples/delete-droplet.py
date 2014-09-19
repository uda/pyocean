from os.path import dirname, abspath
import time
import os
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
import pyocean

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', '')
DROPLET_ID = '12345'

try:
    digitalocean = pyocean.DigitalOcean(ACCESS_TOKEN)
    droplet = digitalocean.droplet.get(DROPLET_ID)
except pyocean.exceptions.DOException as e:
    print('ERROR %s: %s' % (e.code, e.message))
    sys.exit()

while True:
    try:
        droplet.destroy()
        break
    except pyocean.exceptions.DOException as e:
        print('Could not destroy droplet. Reason: %s' % e)

print('Destroyed droplet %s.' % droplet.name)
