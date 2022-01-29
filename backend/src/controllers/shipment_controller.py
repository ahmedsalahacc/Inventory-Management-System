from audioop import add
from flask import Blueprint, request
'''
the file contains the routers the shipment
'''
from models.Shipment import ShipmentModel

from environment.config import config

router = Blueprint("shipment", __name__)

##---- Routes


@router.route("/shipments")
def showAllShipments():
    # @TODO try catch

    dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])

    queries = dbModel.getAll()

    return {
        'code': 200,
        'message': queries
    }


@router.route("/shipments/<id>")
def showShipmentByID(id):
    return"shipment"


@router.route("/shipments", methods=['POST'])
def createShipment():

    # get form data
    name = request.form.get('name')
    status = request.form.get('status')
    shelfIndex = request.form.get('shelfIndex')
    category = request.form.get('category')
    address = request.form.get('address')
    shipperVehicle = request.form.get('shipperVehicle')
    createdDate = 'date'
    shippingTime = request.form.get('shippingTime')
    inventory = request.form.get('inventory')
    shipped_from = request.form.get('shippedFrom')
    shipped_to = request.form.get('shippedTo')
    expected_shipping_date = request.form.get('shippingDate')

    # make data tuples
    data_tuple = (name, status, shelfIndex, category, address,
                  shipperVehicle, createdDate, shippingTime, inventory)
    details = (shipped_from, shipped_to, expected_shipping_date)

    # add to db
    dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])
    dbModel.insert(data_tuple, details)

    return {
        'code': 200,
        'message': 'success'
    }


@router.route("/shipments/<id>", methods=['PUT'])
def updateShipment(id):
    # get form data
    name = request.form.get('name')
    status = request.form.get('status')
    shelfIndex = request.form.get('shelfIndex')
    category = request.form.get('category')
    address = request.form.get('address')
    shipperVehicle = request.form.get('shipperVehicle')
    createdDate = 'date'
    shippingTime = request.form.get('shippingTime')
    inventory = request.form.get('inventory')
    shipped_from = request.form.get('shippedFrom')
    shipped_to = request.form.get('shippedTo')
    expected_shipping_date = request.form.get('shippingDate')

    # make data tuples
    data_tuple = (name, status, shelfIndex, category, address,
                  shipperVehicle, createdDate, shippingTime, inventory)
    details = (shipped_from, shipped_to, expected_shipping_date)

    # add to db
    dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])
    dbModel.update(id, data_tuple, details)

    return {
        'code': 200,
        'message': 'success'
    }


@router.route("/shipments/<id>", methods=['DELETE'])
def deleteShipment(id):
    dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])
    dbModel.delete(id)

    return {
        'code': 200,
        'message': 'success'
    }
