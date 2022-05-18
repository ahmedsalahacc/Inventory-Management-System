class STATUS_CODE:
    BAD_REQUEST = 400
    SUCCESS = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    METHOD_NOT_ALLOWED = 405


def parseMsg(msg):
    '''
    performs rstrip and lstrip on the string

    Parameters:
    -----------
    msg: str - input message

    Returns:
    --------
    parsed_msg: str - the parsed message
    '''
    return msg.rstrip().lstrip() if msg is not None else None
