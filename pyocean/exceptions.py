class DOException(Exception):

    def __init__(self, code=None, msg=None):
        super(DOException, self).__init__(msg)
        self.code = code
        self.message = msg


class AuthException(DOException):

    def __init__(self, code=None, msg=None):
        super(AuthException, self).__init__(code, msg)


class ClientError(DOException):

    def __init__(self, code=None, msg=None):
        super(ClientError, self).__init__(code, msg)


class ServerError(DOException):

    def __init__(self, code=None, msg=None):
        super(ServerError, self).__init__(code, msg)
