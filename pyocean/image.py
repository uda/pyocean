from .base import Resource, ResourceIterator

class Image(Resource):
    
    def __init__(self, attrs={}):
        super(Image, self).__init__(attrs)

    def __str__(self):
        return "<Image '%s' (%s)>" % \
                (self._attrs.get('slug', self._attrs.get('id')), self.name)


class ImageIterator(ResourceIterator):

    def __init__(self, droplet_id=None, image_type=None):
        super(ImageIterator, self).__init__()
        if droplet_id:
            self._resource = 'droplets/%s/%s' % (droplet_id, image_type)
