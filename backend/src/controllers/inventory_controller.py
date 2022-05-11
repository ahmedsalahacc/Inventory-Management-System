from flask import Blueprint, request, abort
'''
This script contains the routers that interface f ff with the inventory model
'''
from models.Inventory import InventoryModel

from environment.config import config
from controllers.utils import checkEmptyOrNone


router = Blueprint("inventory", __name__)
DB_FILENAME = config['DB']['DB_FILEPATH']

##---- Routes


@router.route("/inventories")
def showAllInventories():
    # @TODO try catch
    dbModel = InventoryModel(DB_FILENAME)
    queries = dbModel.getAll()

    return {
        'code': 200,
        'message': queries
    }


@router.route("/inventories", methods=['POST'])
def createInventory():
    # get the form data
    category = request.get_json().get('category', None)
    warehouse_id = request.get_json().get('warehouse_id', None)
    desc = request.get_json().get('desc', None)
    name = request.get_json().get('name', None)

    data = (name, category, desc, warehouse_id)

    # check if there is None in the data (since all required in the db Model) or length < 1
    checkEmptyOrNone(data, lambda: abort(500))

    # add to database
    dbModel = InventoryModel(DB_FILENAME)
    dbModel.insert(data)

    return {
        'code': 200,
        'message': 'success'
    }

# @TODO


@router.route("/inventories/<id>")
def showInventoryByID(id):
    return "Inventory"


@router.route("/inventories/<id>", methods=['PUT'])
def updateInventory(id):
    # get new form data
    category = request.form.get('category', None)
    warehouse_id = request.get_json().get('warehouse_id', None)
    desc = request.get_json().get('desc', None)
    name = request.get_json().get('name', None)

    data = (name, category, desc, warehouse_id)

    # check if there is None in the data (since all required in the db Model)
    checkEmptyOrNone(data, lambda: abort(500))

    # inserting new data in the database
    dbModel = InventoryModel(DB_FILENAME)
    dbModel.update(id, data)

    return {
        'code': 200,
        'message': 'success'
    }


@router.route("/inventories/<id>", methods=['DELETE'])
def deleteInventory(id):

    dbModel = InventoryModel(DB_FILENAME)
    dbModel.delete(id)

    return {
        'code': 200,
        'message': 'success'
    }
