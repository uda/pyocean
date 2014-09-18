class PyoceanException(Exception):

    def __init__(self, msg):
        super(PyoceanException, self).__init__(msg)


class AuthException(PyoceanException):

    def __init__(self, msg="Authentication failed."):
        super(AuthException, self).__init__(msg)


class ClientException(PyoceanException):

    def __init__(self, msg="HTTP error"):
        super(ClientException, self).__init__(msg)


class ServerException(PyoceanException):

    def __init__(self, msg="HTTP error"):
        super(ServerException, self).__init__(msg)
