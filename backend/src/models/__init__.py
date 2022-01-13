from flask_sqlalchemy import SQLAlchemy

'''initialize db to apply factory pattern in flask
    to avoid circuilar imports
'''
db = SQLAlchemy()
