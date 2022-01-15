from flask import Flask, request, redirect, jsonify, url_for, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

'''
app.py: initializes the backend system with the configs in /environment.config
'''
import environment.config as config
from controllers.inventory_controller import router as invRouter
from controllers.warehouse_controller import router as whRouter
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

    # @TODO setting flask configs
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:"+db_filepath

    # Blueprints
    app.register_blueprint(invRouter)
    app.register_blueprint(whRouter)
    return app


# create flask app
app = createFlaskApp()

if __name__ == "__main__":
    # run flask app
    app.run(debug=config.DEBUG, port=config.PORT)
