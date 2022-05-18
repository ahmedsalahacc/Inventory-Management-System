'''
This script contains the routers that interface f ff with the inventory model
'''
from flask import Blueprint, request, abort

from models.Inventory import InventoryModel
from environment.config import config
from controllers.utils import parseMsg, STATUS_CODE

##---- Globals and Constants ----##
router = Blueprint("inventory", __name__)
DB_FILENAME = config['DB']['DB_FILEPATH']
# sets has O(1) search time as it uses hashing to access its values
REQUIRED_KEYS_SET = ('name', 'desc', 'warehouse_id')


##---- Routes ----##
@router.route("/inventory/all")
def showAllInventories():
    try:
        dbModel = InventoryModel(DB_FILENAME)
        queries = dbModel.getAll()

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': queries
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


@router.route("/inventory", methods=['POST'])
def createInventory():
    try:
        data = []

        for key in REQUIRED_KEYS_SET:
            value = parseMsg(request.get_json().get(key, None))

            # check if the value is empty or None
            if value == None or len(value) == 0:
                msg = f'{key} has a value of None or has an empty string'
                abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            data.append(value)

        data = tuple(data)

        # add to database
        dbModel = InventoryModel(DB_FILENAME)
        print(dbModel.insert(data), data)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': 'success'
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


# @TODO


@router.route("/inventory/<id>")
def showInventoryByID(id):
    return "Inventory"


@router.route("/inventory/<id>", methods=['PUT'])
def updateInventory(id):
    try:
        data = []

        for key in REQUIRED_KEYS_SET:
            value = parseMsg(request.get_json().get(key, None))

            # check if the value is empty or None
            if value == None or len(value) == 0:
                msg = f'{key} has a value of None or has an empty string'
                abort(STATUS_CODE.BAD_REQUEST, {'message': msg})

            data.append(value)

        data = tuple(data)

        # inserting new data in the database
        dbModel = InventoryModel(DB_FILENAME)
        dbModel.update(id, data)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': 'success'
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)


@router.route("/inventory/<id>", methods=['DELETE'])
def deleteInventory(id):
    try:
        dbModel = InventoryModel(DB_FILENAME)
        dbModel.delete(id)

        return {
            'code': STATUS_CODE.SUCCESS,
            'message': 'success'
        }
    except:
        abort(STATUS_CODE.INTERNAL_SERVER_ERROR)
