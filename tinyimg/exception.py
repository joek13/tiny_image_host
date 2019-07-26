
class ApiException(Exception):
    status_code = 500
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        resp = dict(self.payload or ())
        resp["status"] = "error"
        resp["message"] = self.message
        return resp

class InvalidToken(ApiException):
    status_code = 401

class MissingImage(ApiException):
    status_code = 400

class ImageTypeNotAllowed(ApiException):
    status_code = 400
