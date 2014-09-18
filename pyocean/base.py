from .exceptions import *
import urlparse
import re
import os
import sys

try:
    import requests
except ImportError:
    print('Please install requests.')
    sys.exit()


class ApiClient(object):

    end_point = 'https://api.digitalocean.com/v2/'

    def __init__(self):
        self.access_token = os.getenv('PYOCEAN_ACCESS_TOKEN')

    def call_api(self, path, method='get', params=None):
        adapter = requests.adapters.HTTPAdapter(max_retries=0)
        sess = requests.Session()
        sess.mount('http', adapter)
        try:
            headers = {}
            if self.access_token:
                headers['Authorization'] = 'Bearer %s' % self.access_token
            f = getattr(sess, method.lower())
            r = f(urlparse.urljoin(self.end_point, path), headers=headers, params=params)
        except requests.exceptions.RequestException as e:
            if type(e) is requests.exceptions.ConnectionError:
                print('ERROR: connection failed.')
            elif type(e) is requests.exceptions.ProxyError:
                print('ERROR: proxy error.')
            elif type(e) is requests.exceptions.Timeout:
                print('ERROR: request timed out.')
            elif type(e) is requests.exceptions.SSLError:
                print('ERROR: SSL error occured.')
            sys.exit()
        else:
            status_code = int(r.status_code)
            try:
                content = r.json()
            except:
                content = {}
            if status_code == 401:
                raise AuthException(content.get('message'))
            return r


class Resource(ApiClient):

    def __init__(self, attrs):
        super(Resource, self).__init__()
        self.__attrs = attrs if type(attrs) is dict else {}

    def __getattr__(self, name):
        if name in self.__attrs:
            return self.__attrs[name]
        else:
            me = self.__class__.__name__
            raise AttributeError("Object '%s' has no attribute '%s'." % (me, name))

    def all(self):
        module = __import__('pyocean')
        return getattr(module, '%sIterator' % self.__class__.__name__)()


class ResourceIterator(ApiClient):

    def __init__(self):
        super(ResourceIterator, self).__init__()
        self.data = []
        self.page = 1
        self.has_more = True
        self.resource = '%ss' % re.sub('Iterator$', '', self.__class__.__name__).lower()

    def __iter__(self):
        return self

    def next(self):
        if not self.data and self.has_more:
            r = self.call_api(self.resource, params={'page': self.page})
            d = r.json()
            try:
                self.data = d[self.resource] or d[self.resource[:-1]]
            except KeyError:
                self.data = None
            try:
                self.has_more = bool(d['links']['pages']['next'])
            except KeyError:
                self.has_more = False
            self.page += 1

        if self.data:
            module = __import__('pyocean')
            class_ = getattr(module, self.resource[:-1].capitalize())
            return class_(self.data.pop(0))
        else:
            raise StopIteration
