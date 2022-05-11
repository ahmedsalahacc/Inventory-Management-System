from flask import Blueprint, redirect, request, abort
'''
the file contains the routers of the warehouse
'''
from models.Warehouse import WarehouseModel

from environment.config import config
from controllers.utils import checkEmptyOrNone

router = Blueprint("warehouse", __name__)
DB_FILENAME = config['DB']['DB_FILEPATH']

##---- Routes


@router.route('/')
def home():
    return redirect('/warehouses')


@router.route("/warehouse/all")
def showAllWarehouses():

    # @TODO try catch
    dbModel = WarehouseModel(config['DB']['DB_FILEPATH'])

    queries = dbModel.getAll()

    return {
        'code': 200,
        'message': queries
    }


@router.route("/warehouse", methods=['POST'])
def createWarehouse():
    # get the form data
    name = request.get_json().get('name', None)
    location = request.get_json().get('location', None)
    data = (name, location)
    print(request.get_json())

    # check if there is None in the data (since all required in the db Model) or length < 1
    checkEmptyOrNone(data, lambda: abort(500))

    # add to database
    dbModel = WarehouseModel(DB_FILENAME)
    dbModel.insert(data)

    return {
        'code': 200,
        'message': 'success'
    }

# @TODO


@router.route("/warehouse/<id>")
def showWareHouseByID(id):
    dbModel = WarehouseModel(DB_FILENAME)
    return "Warehouse"


@router.route("/warehouse/<id>", methods=['PUT'])
def updateWarehouse(id):
    # get the form data
    name = request.form.get('name', None)
    location = request.form.get('location', None)
    data = (name, location)

    # check if there is None in the data (since all required in the db Model)
    if None in data:
        print('None in data')
        abort(500)

    # add to database
    dbModel = WarehouseModel(DB_FILENAME)
    dbModel.update(id, data)

    return {
        'code': 200,
        'message': 'success'
    }


@router.route("/warehouse/<id>", methods=['DELETE'])
def deleteWareHouse(id):

    dbModel = WarehouseModel(DB_FILENAME)
    dbModel.delete(id)

    return {
        'code': 200,
        'message': 'success'
    }
