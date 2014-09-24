class DOException(Exception):
    """Base exception for pyocean package."""

    def __init__(self, msg=None, code=None):
        super(DOException, self).__init__(msg)
        self.message = msg
        self.code = code


class ClientError(DOException):
    """HTTP 4xx error"""

class ServerError(DOException):
    """HTTP 5xx error"""

class AuthException(DOException):
    pass

class InvalidResponse(DOException):
    pass

class DropletActionError(DOException):
    pass

class ImageActionError(DOException):
    pass
