from .exceptions import *
import pyocean
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

    def call_api(self, path, method='get', params=None, data=None):
        adapter = requests.adapters.HTTPAdapter(max_retries=0)
        sess = requests.Session()
        sess.mount('http', adapter)
        try:
            headers = {}
            if self.access_token:
                headers['Authorization'] = 'Bearer %s' % self.access_token
            f = getattr(sess, method.lower())
            r = f(urlparse.urljoin(self.end_point, path), headers=headers, params=params, data=data)
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
            try:
                content = r.json()
            except:
                content = {}
            status_code = int(r.status_code)
            if status_code >= 500:
                raise ServerException(content.get('message'))
            elif status_code >= 400:
                raise ClientException(content.get('message'))
            return content


class Resource(ApiClient):

    def __init__(self, attrs):
        super(Resource, self).__init__()
        self.__attrs = attrs if type(attrs) is dict else {}
        self.__classname = self.__class__.__name__
        self.__resource = '%ss' % self.__classname.lower()

    def __getattr__(self, name):
        if name in self.__attrs:
            return self.__attrs[name]
        else:
            msg = "'%s' object has no attribute '%s'." % (self.__classname, name)
            raise AttributeError(msg)

    def all(self):
        return getattr(pyocean, '%sIterator' % self.__classname)()

    def create(self, attrs):
        data = self.call_api(self.__resource, method='post', data=attrs)
        attr = data[self.__resource[:-1]]
        return getattr(pyocean, self.__classname)(attr)

    def destroy(self):
        if self.__attrs.get('id'):
            path = '%s/%s' % (self.__resource, self.__attrs['id'])
            data = self.call_api(path, method='delete')
        else:
            raise ValueError('Droplet is not loaded.')


class ResourceIterator(ApiClient):

    def __init__(self):
        super(ResourceIterator, self).__init__()
        self.__data = []
        self.__page = 1
        self.__has_more = True
        self.__classname = self.__class__.__name__
        self.__resource = '%ss' % re.sub('Iterator$', '', self.__classname).lower()

    def __iter__(self):
        return self

    def next(self):
        if not self.__data and self.__has_more:
            content = self.call_api(self.__resource, params={'page': self.__page})
            try:
                self.__data = content[self.__resource]
            except KeyError:
                self.__data = None
            try:
                self.__has_more = bool(content['links']['pages']['next'])
            except KeyError:
                self.__has_more = False
            self.__page += 1

        if self.__data:
            clas = getattr(pyocean, self.__resource[:-1].capitalize())
            return clas(self.__data.pop(0))
        else:
            raise StopIteration
