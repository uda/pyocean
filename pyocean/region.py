from .base import Resource, ResourceIterator


class Region(Resource):

    def __init__(self, attrs={}):
        super(Region, self).__init__(attrs)

    def get(self, *args, **kwargs):
        raise AttributeError("'Region' object has no attribute 'get'.")

    def create(self, *args, **kwargs):
        raise AttributeError("'Region' object has no attribute 'create'.")

    def destroy(self, *args, **kwargs):
        raise AttributeError("'Region' object has no attribute 'create'.")

    def __str__(self):
        return "<Region '%s' (%s)>" % (self.slug, self.name)


class RegionIterator(ResourceIterator):

    def __init__(self):
        super(RegionIterator, self).__init__()

