import pyocean
import os

class DigitalOcean(object):

    # Available classes
    classes = ['droplet',
               'image',
               'action',
               'size',
               'region']

    def __init__(self, access_token):
        self.access_token = access_token
        os.environ['PYOCEAN_ACCESS_TOKEN'] = access_token

    def __getattr__(self, attr):
        if attr in self.classes:
            return getattr(pyocean, attr.capitalize())()
        else:
            me = self.__class__.__name__
            raise AttributeError("'%s' object has no attribute '%s'" % (me, attr))
