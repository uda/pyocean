from .base import Resource, ResourceIterator


class Action(Resource):

    def __init__(self, attrs={}):
        super(Action, self).__init__(attrs)


class ActionIterator(ResourceIterator):

    def __init__(self):
        super(ActionIterator, self).__init__()
