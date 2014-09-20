from .base import ApiClient
from .exceptions import InvalidResponse


class DropletAction(ApiClient):

    def __init__(self, droplet_id, attrs={}):
        super(DropletAction, self).__init__()
        self.__attrs = attrs
        self.__droplet_id = droplet_id

    def __getattr__(self, name):
        if name is 'status':
            res = self.call_api('droplets/%s/actions/%s' % (self.__droplet_id, self.id))
            try:
                status = res['action']['status']
            except KeyError:
                raise InvalidResponse('Retrieved invalid response from DigitalOcean API.')
            else:
                self.__attrs = res['action']
                return status
        elif name in self.__attrs:
            return self.__attrs[name]
        else:
            msg = "'%s' object has no attribute '%s'." % (self.__classname, name)
            raise AttributeError(msg)

    def __str__(self):
        return '<DropletAction %s (%s)>' % (self.id, self.type)
