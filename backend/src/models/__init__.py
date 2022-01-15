import os
import sqlite3
'''initialize db to apply factory pattern in flask
    to avoid circuilar imports
'''
from environment import config


class DBinit:
    def init_db(self):
        '''
        Initializes Database and creates all tables
        '''
        cwd = os.getcwd()
        db_dirname = 'dbfiles'
        db_filename = config.DB_FILE_NAME

        # check if the db folder exists
        db_dirpath = self.__checkDBModelDir(cwd, db_dirname)
        db_filepath = os.path.join(db_dirpath, db_filename)

        # connect to db and execute script
        conn = sqlite3.connect(db_filepath)
        cursor = conn.cursor()
        self.__writeTables(conn, cursor)

        conn.close()

        return db_filepath

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
        sql_script_shipment = '''
        CREATE TABLE shipment (
            id CHARACTER(10) NOT NULL PRIMARY KEY,
            name text NOT NULL,
            status Character(10) NOT NULL,
            shelfIndex Text NOT NULL,
            category TEXT NOT NULL,
            description Text NULL,
            shipper_vehicle_id NUMBER NULL,
            created_date TEXT NOT NULL,
            shipping_time TEXT NULL
        );
        '''

        sql_script_sh_data = '''
        CREATE TABLE shipment_data(
            id CHARACTER(10) NOT NULL PRIMARY KEY,
            shipped_from TEXT NOT NULL,
            shipped_to TEXT NOT NULL,
            expected_shipping_date  TEXT NOT NULL,
            shipment_id CHARACTER(10),
            FOREIGN KEY(shipment_id) REFERENCES shipment(id)
        );
        '''

        sql_script_inventory = '''
        CREATE TABLE inventory(
            id CHARACTER(10) NOT NULL PRIMARY KEY,
            category TEXT NOT NULL,
            shipment_id CHARACTER(10),
            FOREIGN KEY(shipment_id) REFERENCES shipment(id)
        );
        '''

        sql_script_wh = '''
        CREATE TABLE warehouse(
            id CHARACTER(10) NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            inventory_id CHARACTER(10) NULL,
            FOREIGN KEY(inventory_id) REFERENCES inventory(id)
        );
        '''

        # execute and commit
        try:
            cursor.execute(sql_script_shipment)
            print("[DB Setting] Successfully created table shipment")
        except:
            print("[DB Setting] table shipment already exists or some error occured")
        try:
            cursor.execute(sql_script_sh_data)
            print("[DB Setting] Successfully created table shipment_data")
        except:
            print(
                "[DB Setting] table shipment_data already exists or some error occured")
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
