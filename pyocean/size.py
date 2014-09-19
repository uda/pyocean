from .base import Resource, ResourceIterator


class Size(Resource):

    def __init__(self, attrs={}):
        super(Size, self).__init__(attrs)

    def get(self, *args, **kwargs):
        raise AttributeError("'Size' object has no attribute 'get'.")

    def create(self, *args, **kwargs):
        raise AttributeError("'Size' object has no attribute 'create'.")

    def destroy(self, *args, **kwargs):
        raise AttributeError("'Size' object has no attribute 'create'.")


class SizeIterator(ResourceIterator):

    def __init__(self):
        super(SizeIterator, self).__init__()

