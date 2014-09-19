from .base import Resource, ResourceIterator


class Action(Resource):

    def __init__(self, attrs={}):
        super(Action, self).__init__(attrs)

    def create(self, *args, **kwargs):
        raise AttributeError("'Action' object has no attribute 'create'.")

    def destroy(self, *args, **kwargs):
        raise AttributeError("'Action' object has no attribute 'create'.")


class ActionIterator(ResourceIterator):

    def __init__(self):
        super(ActionIterator, self).__init__()
