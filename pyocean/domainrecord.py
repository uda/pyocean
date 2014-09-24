from .base import Resource, ResourceIterator
from .exceptions import InvalidResponse

class DomainRecord(Resource):

    def __init__(self, attrs, parent):
        super(DomainRecord, self).__init__(attrs, parent)
        self._json_key = 'domain_records'
        self._resource = 'domains/%s/records' % parent

    def rename(self, name):
        path = '%s/%s' % (self._resource, self.id)
        res = self.call_api(path, method='put', data={'name': name})
        try:
            self._attrs = res['domain_record']
            return self
        except KeyError:
            raise InvalidResponse('Retrieved invalid response from the API.')

    def delete(self):
        return self.destroy()

    def __str__(self):
        if self.name:
            return "<DomainRecord '%s' (%s, %s)>" % (self.type, self.name, self.data)
        else:
            return "<DomainRecord '%s' (%s)>" % (self.type, self.data)


class DomainRecordIterator(ResourceIterator):

    def __init__(self, domain):
        super(DomainRecordIterator, self).__init__(domain)
        self._json_key = 'domain_records'
        self._resource = 'domains/%s/records' % domain
