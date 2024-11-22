from rest_framework.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

class Unauthorized(APIException):
    status_code = 401
    default_detail = 'Invalid credential'
    default_code = 'UNAUTHORIZED'

class BadRequest(APIException):
    status_code = 400
    default_detail = 'bad request'
    default_code = 'BAD_REQUEST'