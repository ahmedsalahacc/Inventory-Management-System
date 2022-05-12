'''
the file contains the routers the shipment
'''
from flask import Blueprint, request, abort

from models.Shipment import ShipmentModel
from environment.config import config
from controllers.utils import checkEmptyOrNone

router = Blueprint("shipment", __name__)

##---- Routes


@router.route("/shipment/all")
def showAllShipments():
    # @TODO try catch

    dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])

    queries = dbModel.getAll()

    return {
        'code': 200,
        'message': queries
    }

# @TODO


@router.route("/shipment/<id>")
def showShipmentByID(id):
    return"shipment"


@router.route("/shipment", methods=['POST'])
def createShipment():

    # get form data
    name = request.get_json().get('name')
    shelfIndex = request.get_json().get('shelfIndex')
    category = request.get_json().get('category')
    status = request.get_json().get('status')
    shipperVehicle = request.get_json().get('shipperVehicle')
    shipped_from = request.get_json().get('shippedFrom')
    shipped_to = request.get_json().get('shippedTo')
    expected_shipping_date = request.get_json().get('shippingDate')
    shippingTime = request.get_json().get('shippingTime')
    createdDate = 'date'
    address = request.get_json().get('address')
    inventory = request.get_json().get('inventory')

    # make data tuples
    data = (name, status, shelfIndex, category, address,
            shipperVehicle, createdDate, inventory)
    details = (shipped_from, shipped_to, expected_shipping_date, shippingTime)

    # check if there is None in the data (since all required in the db Model) or length < 1
    # checkEmptyOrNone(data, lambda: abort(500))

    # check if there is None in the data (since all required in the db Model) or length < 1
    # checkEmptyOrNone(details, lambda: abort(500))

    # add to db
    dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])
    dbModel.insert(data, details)

    return {
        'code': 200,
        'message': 'success'
    }


@router.route("/shipment/<id>", methods=['PUT'])
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
                  shipperVehicle, createdDate, inventory)
    details = (shipped_from, shipped_to, expected_shipping_date)

    # checkEmptyOrNone(data_tuple, lambda: abort(500))
    # checkEmptyOrNone(details, lambda: abort(500))

    # add to db
    dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])
    dbModel.update(id, data_tuple, details)

    return {
        'code': 200,
        'message': 'success'
    }


@router.route("/shipment/<id>", methods=['DELETE'])
def deleteShipment(id):
    dbModel = ShipmentModel(config['DB']['DB_FILEPATH'])
    dbModel.delete(id)

    return {
        'code': 200,
        'message': 'success'
    }
