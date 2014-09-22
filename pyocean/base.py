import urlparse
import re
import os
import sys
import os.path
import pyocean
from .exceptions import *

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
                raise ServerError(content.get('message'), status_code)
            elif status_code >= 400:
                raise ClientError(content.get('message'), status_code)
            return content


class Resource(ApiClient):

    def __init__(self, attrs):
        super(Resource, self).__init__()
        self._attrs = attrs if type(attrs) is dict else {}
        self._classname = self.__class__.__name__
        self._resource = '%ss' % self._classname.lower()

    def __getattr__(self, name):
        if name in self._attrs:
            return self._attrs[name]
        else:
            msg = "'%s' object has no attribute '%s'." % (self._classname, name)
            raise AttributeError(msg)

    def all(self):
        return getattr(pyocean, '%sIterator' % self._classname)()

    def get(self, resource_id):
        data = self.call_api('%s/%s' % (self._resource, str(resource_id)))
        attr = data[self._resource[:-1]]
        return getattr(pyocean, self._classname)(attr)

    def create(self, attrs):
        data = self.call_api(self._resource, method='post', data=attrs)
        attr = data[self._resource[:-1]]
        return getattr(pyocean, self._classname)(attr)

    def destroy(self):
        if self._attrs.get('id'):
            path = '%s/%s' % (self._resource, self._attrs['id'])
            data = self.call_api(path, method='delete')
        else:
            raise ValueError('Droplet is not loaded.')


class ResourceIterator(ApiClient):

    def __init__(self):
        super(ResourceIterator, self).__init__()
        self._data = []
        self._page = 1
        self._has_more = True
        self._classname = re.sub('Iterator$', '', self.__class__.__name__)
        self._resource = '%ss' % self._classname.lower()

    def __iter__(self):
        return self

    def next(self):
        if not self._data and self._has_more:
            content = self.call_api(self._resource, params={'page': self._page})
            try:
                key = os.path.basename(re.sub('/\d+', '', self._resource))
                self._data = content[key]
            except KeyError:
                self._data = None
            try:
                self._has_more = bool(content['links']['pages']['next'])
            except KeyError:
                self._has_more = False
            self._page += 1

        if self._data:
            c = getattr(pyocean, self._classname)
            return c(self._data.pop(0))
        else:
            raise StopIteration
