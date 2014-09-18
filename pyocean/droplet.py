from .base import Resource, ResourceIterator


class Droplet(Resource):

    def __init__(self, attrs={}):
        super(Droplet, self).__init__(attrs)


class DropletIterator(ResourceIterator):

    def __init__(self):
        super(DropletIterator, self).__init__()
