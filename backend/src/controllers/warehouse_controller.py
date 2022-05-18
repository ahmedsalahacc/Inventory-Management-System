'''
the file contains the routers of the warehouse
'''
from flask import Blueprint, redirect, request, abort

from models.Warehouse import WarehouseModel
from environment.config import config
from controllers.utils import parseMsg, STATUS_CODE

##---- Globals and Constants ----##
router = Blueprint("warehouse", __name__)
DB_FILENAME = config['DB']['DB_FILEPATH']
REQUIRED_KEYS_SET = ('name', 'location')

##---- Routes ----##


@router.route('/')
def home():
    return "Welcome to Manageeto"


@router.route("/warehouse/all")
def showAllWarehouses():

    try:

        dbModel = WarehouseModel(config['DB']['DB_FILEPATH'])

        queries = dbModel.getAll()

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': queries
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


@router.route("/warehouse", methods=['POST'])
def createWarehouse():
    try:
        data = []

        for key in REQUIRED_KEYS_SET:
            value = request.get_json().get(key, None)

            if value == None or len(value) == 0:
                msg = f'{key} has a value of None or has an empty string'
                abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            data.append(value)

        data = tuple(data)

        # add to database
        dbModel = WarehouseModel(DB_FILENAME)
        dbModel.insert(data)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': 'success'
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


@router.route("/warehouse/<id>")
def showWareHouseByID(id):
    try:
        dbModel = WarehouseModel(DB_FILENAME)
        data = dbModel.getByID(id)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': data
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


@router.route("/warehouse/<id>", methods=['PUT'])
def updateWarehouse(id):
    try:
        data = []

        for key in REQUIRED_KEYS_SET:
            value = request.get_json().get(key, None)

            if value == None or len(value) == 0:
                msg = f'{key} has a value of None or has an empty string'
                abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            data.append(value)

        data = tuple(data)

        # add to database
        dbModel = WarehouseModel(DB_FILENAME)
        dbModel.update(id, data)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': 'success'
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


@router.route("/warehouse/<id>", methods=['DELETE'])
def deleteWareHouse(id):
    try:
        dbModel = WarehouseModel(DB_FILENAME)
        dbModel.delete(id)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': 'success'
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)
