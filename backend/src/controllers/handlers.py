from http.client import METHOD_NOT_ALLOWED
from flask import Blueprint
'''
This file has the error handlers of the invalid requests
'''

handler = Blueprint("handler", __name__)

####------ STATUS CODES-------####
BAD_REQUEST = 500
NOT_FOUND = 404
METHOD_NOT_ALLOWED = 405
####--------------------------####

##---- Routes


@handler.app_errorhandler(BAD_REQUEST)
def handle_500(e):
    return {
        'message': 'bad request',
        'code': BAD_REQUEST
    }, BAD_REQUEST


@handler.app_errorhandler(NOT_FOUND)
def hanfle_404(e):
    return {
        'message': 'page not found',
        'code': NOT_FOUND
    }, NOT_FOUND


@handler.app_errorhandler(METHOD_NOT_ALLOWED)
def hanfle_405(e):
    return {
        'message': 'method not allowed',
        'code': METHOD_NOT_ALLOWED
    }, METHOD_NOT_ALLOWED
