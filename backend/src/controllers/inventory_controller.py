from flask import Blueprint, request, abort
'''
This script contains the routers that interface f ff with the inventory model
'''
from models.Inventory import InventoryModel

from environment.config import config

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
    category = request.form.get('category', None)
    warehouse_id = request.form.get('warehouse_id', None)
    desc = request.form.get('desc', None)
    name = request.form.get('name', None)

    data = (name, category, desc, warehouse_id)

    # check if there is None in the data (since all required in the db Model)
    if None in (name, category, warehouse_id):
        print('None in data')
        abort(500)

    # add to database
    dbModel = InventoryModel(DB_FILENAME)
    dbModel.insert(data)

    return {
        'code': 200,
        'message': 'success'
    }


@router.route("/inventories/<id>")
def showInventoryByID(id):
    return "Inventory"


@router.route("/inventories/<id>", methods=['PUT'])
def updateInventory(id):
    # get new form data
    category = request.form.get('category', None)
    warehouse_id = request.form.get('warehouse_id', None)
    desc = request.form.get('desc', None)
    name = request.form.get('name', None)

    data = (name, category, desc, warehouse_id)

    # check if there is None in the data (since all required in the db Model)
    if None in (name, category, warehouse_id):
        print('None in data')
        abort(500)

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
