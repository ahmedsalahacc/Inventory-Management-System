from flask import Flask, request, redirect, jsonify, url_for, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

'''
app.py: initializes the backend system with the configs in /environment.config
'''

from environment.config import config
from models import DBinit

import os


def createFlaskApp() -> tuple:
    '''
    Create a flask app with the predefined settings

    Returns
    -------
    app : Flask
        initialized flask app with the predefined settings 
    '''
    # create flask app
    app = Flask(__name__)

    # inititalizing extensions
    CORS(app)
    db_init = DBinit()
    db_filepath = db_init.init_db()

    # updating db path in config dict
    config['DB']['DB_FILEPATH'] = db_filepath

    # setting flask configs
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:"+db_filepath

    # Blueprints
    from controllers.inventory_controller import router as invRouter
    from controllers.warehouse_controller import router as whRouter
    from controllers.shipment_controller import router as shRouter
    from controllers.handlers import handler

    app.register_blueprint(invRouter)
    app.register_blueprint(whRouter)
    app.register_blueprint(shRouter)
    app.register_blueprint(handler)

    # random tests
    from models.seed import seedWarehouseData, seedInventoryData, seedShipmentData
    # seedWarehouseData()
    # seedInventoryData()
    # seedShipmentData()
    return app


# create flask app
app = createFlaskApp()

if __name__ == "__main__":
    # run flask app
    app.run(debug=config['ENV']['DEBUG'], port=config['ENV']['PORT'])
