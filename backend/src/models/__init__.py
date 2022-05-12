import os
import sqlite3
import uuid
'''
contains the initialization of the base tables
wrote sql instead of using sqlalchemy to demonstrate my SQL skill
'''
from environment.config import config


def gen_id():
    return str(uuid.uuid4())[:10]


class BaseModel:
    def __init__(self, db_filepath):
        self.db_filepath = db_filepath

        # Establishing connection
        try:
            self.conn = sqlite3.connect(self.db_filepath)
        except Exception as e:
            print(e)

    def insert(self):
        ''' Inserts item into the database'''
        raise NotImplementedError

    def delete(self):
        ''' Deletes item from the database'''
        raise NotImplementedError

    def update(self):
        ''' Updates a record in the database'''
        raise NotImplementedError

    def get(self):
        ''' Gets a record from the database'''
        raise NotImplementedError


class DBinit:
    def init_db(self):
        '''
        Initializes Database and creates all tables
        '''
        cwd = os.getcwd()
        db_dirname = 'dbfiles'
        print(config['DB'])
        db_filename = config['DB']['DB_FILE_NAME']

        # check if the db folder exists
        db_dirpath = self.__checkDBModelDir(cwd, db_dirname)
        db_filepath = os.path.join(db_dirpath, db_filename)

        # connect to db and execute script
        conn = sqlite3.connect(db_filepath)
        cursor = conn.cursor()
        self.__writeTables(conn, cursor)

        conn.close()

        return db_filepath

    def __checkDBModelDir(self, path: str, dirname: str):
        '''
        Checks the existence of the database directory

        Parameters
        ----------
        path: str
            path of the current directory
        dirname: str
            database directory name

        Returns
        -------

        path: str
            database directory path
        '''
        path = os.path.join(path, dirname)
        if not os.path.isdir(path):
            os.mkdir(path)
            print(f"[DB Setting] Successfully DB dir at {path}")
        print("[DB Setting] DB dir already exists")

        return path

    def __writeTables(self, connection: sqlite3.Connection, cursor: sqlite3.Connection.cursor):
        '''
        Builds the database tables with an internal script

        Parameters
        ----------
        connection: sqlite3.Connection
            db connection object
        cursor: sqlite.Connection.cursor
            db cursor object
        '''

        # sql scripts
        sql_script_wh = '''
        CREATE TABLE warehouse(
            id CHARACTER(10) NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        );
        '''

        sql_script_inventory = '''
        CREATE TABLE inventory(
            id CHARACTER(10) NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            desc TEXT NULL,
            warehouse_id CHARACTER(10) NULL,
            FOREIGN KEY(warehouse_id) REFERENCES warehouse(id) ON DELETE CASCADE
        );
        '''
        # @TODO make desc -> address
        sql_script_shipment = '''
        CREATE TABLE shipment (
            id CHARACTER(10) NOT NULL PRIMARY KEY,
            name text NOT NULL,
            status Character(10) NOT NULL,
            shelfIndex Text NOT NULL,
            category TEXT NOT NULL,
            address NOT NULL,
            shipper_vehicle_id NUMBER NULL,
            created_date TEXT NOT NULL,
            inventory_id CHARACTER(10) NOT NULL,
            shipment_details_id CHARACTER(10) NOT NULL,
            FOREIGN KEY(inventory_id) REFERENCES inventory(id) ON DELETE CASCADE,
            FOREIGN KEY(shipment_details_id) REFERENCES shipment_details(id) ON DELETE CASCADE
        );
        '''

        sql_script_sh_data = '''
        CREATE TABLE shipment_details(
            id CHARACTER(10) NOT NULL PRIMARY KEY,
            shipped_from TEXT NOT NULL,
            shipped_to TEXT NOT NULL,
            expected_shipping_date  TEXT NOT NULL, 
            shipping_time TEXT NOT NULL
        );
        '''

        # execute and commit

        try:
            cursor.execute(sql_script_sh_data)
            print("[DB Setting] Successfully created table shipment_details")
        except:
            print(
                "[DB Setting] table shipment_data already exists or some error occured")
        try:
            cursor.execute(sql_script_shipment)
            print("[DB Setting] Successfully created table shipment")
        except:
            print("[DB Setting] table shipment already exists or some error occured")
        try:
            cursor.execute(sql_script_inventory)
            print("[DB Setting] Successfully created table inventory")
        except:
            print(
                "[DB Setting] table inventory already exists or some error occured")
        try:
            cursor.execute(sql_script_wh)
            print("[DB Setting] Successfully created table warehouse")
        except:
            print("[DB Setting] table warehouse already exists or some error occured")

        connection.commit()
        cursor.close()
