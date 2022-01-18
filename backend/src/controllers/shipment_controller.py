from flask import Blueprint
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

    return "Shipment"


@router.route("/shipments/<id>", methods=['POST'])
def createShipment(id):
    return "Shipment"


@router.route("/shipments/<id>", methods=['PUT'])
def updateShipment(id):
    return "Shipment"


@router.route("/shipments/<id>", methods=['DELETE'])
def deleteShipment(id):
    return "Shipment"
