from flask import Blueprint
from controllers.utils import STATUS_CODE
'''
This file has the error handlers of the invalid requests
'''

handler = Blueprint("handler", __name__)

DEFAULT_MESSAGE = 'Check request format or contact the developers'
##---- Routes


@handler.app_errorhandler(STATUS_CODE.BAD_REQUEST)
def handle_400(e):
    return {
        'message': 'bad request',
        'code': STATUS_CODE.BAD_REQUEST,
        'desc': e.description.get('message', DEFAULT_MESSAGE)
    }, STATUS_CODE.BAD_REQUEST


@handler.app_errorhandler(STATUS_CODE.NOT_FOUND)
def handle_404(e):
    return {
        'message': 'page not found',
        'code': STATUS_CODE.NOT_FOUND,
        'desc': e.description.get('message', DEFAULT_MESSAGE)
    }, STATUS_CODE.NOT_FOUND


@handler.app_errorhandler(STATUS_CODE.METHOD_NOT_ALLOWED)
def handle_405(e):
    return {
        'message': 'method not allowed',
        'code': STATUS_CODE.METHOD_NOT_ALLOWED,
        'desc': e.description.get('message', DEFAULT_MESSAGE)
    }, STATUS_CODE.METHOD_NOT_ALLOWED


@handler.app_errorhandler(STATUS_CODE.INTERNAL_SERVER_ERROR)
def handle_500(e):
    return{
        'message': 'internal server error',
        'code': STATUS_CODE.INTERNAL_SERVER_ERROR,
        'desc': e.description.get('message', DEFAULT_MESSAGE)
    }, STATUS_CODE.INTERNAL_SERVER_ERROR
