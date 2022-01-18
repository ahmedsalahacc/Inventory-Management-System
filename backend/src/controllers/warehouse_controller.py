from flask import Blueprint, redirect, request, abort
'''
the file contains the routers of the warehouse
'''
from models.Warehouse import WarehouseModel

from environment.config import config

router = Blueprint("warehouse", __name__)
DB_FILENAME = config['DB']['DB_FILEPATH']

##---- Routes


@router.route('/')
def home():
    return redirect('/warehouses')


@router.route("/warehouses")
def showAllWarehouses():

    # @TODO try catch
    dbModel = WarehouseModel(config['DB']['DB_FILEPATH'])

    queries = dbModel.getAll()

    return {
        'code': 200,
        'message': queries
    }


@router.route("/warehouses", methods=['POST'])
def createWarehouse():
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
    dbModel.insert(data)

    return {
        'code': 200,
        'message': 'success'
    }


@router.route("/warehouses/<id>")
def showWareHouseByID(id):
    return "Warehouse"


@router.route("/warehouses/<id>", methods=['PUT'])
def updateWarehouse(id):
    return "Warehouse"


@router.route("/warehouses/<id>", methods=['DELETE'])
def deleteWareHouse(id):
    return "Warehouse"
