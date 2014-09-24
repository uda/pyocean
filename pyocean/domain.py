from .base import Resource, ResourceIterator
from .domainrecord import DomainRecord, DomainRecordIterator
from .exceptions import InvalidResponse


class Domain(Resource):

    def __init__(self, attrs={}):
        super(Domain, self).__init__(attrs)

    def records(self):
        return DomainRecordIterator(self.name)

    def get_record(self, record_id):
        """Get a single record from this domain."""
        try:
            res = self.call_api('domains/%s/records/%s' % (self.name, str(record_id)))
            return DomainRecord(res['domain_record'], self.name)
        except KeyError:
            raise InvalidResponse('Retrieved invalid response from the API.')

    def add_record(self, attrs={}):
        """Create a new record to this domain."""
        try:
            res = self.call_api('domains/%s/records' % self.name, method='post', data=attrs)
            return DomainRecord(res['domain_record'], self.name)
        except KeyError:
            raise InvalidResponse('Retrieved invalid response from the API.')

    def __str__(self):
        return "<Domain '%s'>" % self.name


class DomainIterator(ResourceIterator):

    def __init__(self):
        super(DomainIterator, self).__init__()
