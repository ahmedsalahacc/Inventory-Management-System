def checkEmptyOrNone(data: iter, handler: callable):
    '''
    checks if there is None/Null in data or if there is an empty value

    Parameters:
    -----------
    data: iter - data tuple
    handler: function - handler function (flask abort)
    '''
    if None in data or any([len(i.replace(' ', '')) < 1 for i in data]):
        print('None in data')
        handler()
