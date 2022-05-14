'''
the file contains the routers the shipment
'''
from datetime import datetime
from flask import Blueprint, request, abort

from models.Shipment import ShipmentModel
from environment.config import config
from controllers.utils import parseMsg, STATUS_CODE

##---- Globals and Constants ----##
router = Blueprint("shipment", __name__)
DATA_KEYS_SET = ('name', 'status', 'shelfIndex',
                 'category', 'address', 'shipperVehicle',
                 'date', 'inventory', )

DETAILS_KEYS_SET = ('shippedFrom', 'shippedTo', 'shippingDate', 'shippingTime')

# sets has O(1) search time as it uses hashing to access its values
REQUIRED_KEYS_SET = {'name', 'shelfIndex',
                     'category', 'status',
                     'shippedFrom', 'shippedTo',
                     'shippingDate', 'address',
                     'inventory'}

##---- Routes ----##


@router.route("/shipment/all")
def showAllShipments():
    try:
        dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])

        queries = dbModel.getAll()

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': queries
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


# @TODO


@router.route("/shipment/<id>")
def showShipmentByID(id):
    return"shipment"


@router.route("/shipment", methods=['POST'])
def createShipment():
    try:
        data = []
        details = []

        crt_date = datetime.today().strftime('%Y-%m-%d')

        for key in DATA_KEYS_SET:
            value = parseMsg(request.get_json().get(key, None))

            if key in REQUIRED_KEYS_SET:
                if value == None or len(value) == 0:
                    msg = f'{key} has a value of None or has an empty string'
                    abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            if key == 'date':
                value = crt_date

            data.append(value)

        for key in DETAILS_KEYS_SET:
            value = parseMsg(request.get_json().get(key, None))

            if key in REQUIRED_KEYS_SET:
                if value == None or len(value) == 0:
                    msg = f'{key} has a value of None or has an empty string'
                    abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            # check if the shippingDate less than the current date
            if key == 'shippingDate' and \
                    datetime.strptime(value, '%Y-%m-%d') < \
                    datetime.strptime(crt_date, '%Y-%m-%d'):
                msg = 'Shipment date must be NO earlier than the current date'
                abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            details.append(value)

        data = tuple(data)
        details = tuple(details)

        # add to db
        dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])
        dbModel.insert(data, details)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': 'success'
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


@router.route("/shipment/<id>", methods=['PUT'])
def updateShipment(id):
    try:
        data = []
        details = []

        crt_date = datetime.today().strftime('%Y-%m-%d')

        for key in DATA_KEYS_SET:
            value = parseMsg(request.get_json().get(key, None))

            if key in REQUIRED_KEYS_SET:
                if value == None or len(value) == 0:
                    msg = f'{key} has a value of None or has an empty string'
                    abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            if key == 'date':
                value = crt_date

            data.append(value)

        for key in DETAILS_KEYS_SET:
            value = parseMsg(request.get_json().get(key, None))

            if key in REQUIRED_KEYS_SET:
                if value == None or len(value) == 0:
                    msg = f'{key} has a value of None or has an empty string'
                    abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            # check if the shippingDate less than the current date
            if key == 'shippingDate' and \
                    datetime.strptime(value, '%Y-%m-%d') < \
                    datetime.strptime(crt_date, '%Y-%m-%d'):
                msg = 'Shipment date must be NO earlier than the current date'
                abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            details.append(value)

        data = tuple(data)
        details = tuple(details)

        # add to db
        dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])
        dbModel.update(id, data, details)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': 'success'
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


@router.route("/shipment/<id>", methods=['DELETE'])
def deleteShipment(id):
    try:
        dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])
        dbModel.delete(id)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': 'success'
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)
