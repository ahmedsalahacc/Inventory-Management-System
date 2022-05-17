from models import BaseModel, gen_id


class _ShipmentDetailsModel(BaseModel):
    '''
    ORM for shipment_details table with the following structure

    shipment_details(
        id CHARACTER(10) NOT NULL PRIMARY KEY,
        shipped_from TEXT NOT NULL,
        shipped_to TEXT NOT NULL,
        expected_shipping_date  TEXT NOT NULL,
        shipping_time  TEXT NOT NULL,
    );
    '''

    def __init__(self, db_filename: str):
        super(_ShipmentDetailsModel, self).__init__(db_filename)

    def insert(self, data_tuple: tuple):
        '''
        Inserts a new record in shipment_details table

        Parameters
        ----------
        data_tuple: tuple
            tuple of new values in the form of 
            (shipped_from , shipped_to, expected_shipping_date, shipping_time)

        Returns
        -------
        id: int
            id of the saved record
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        INSERT INTO shipment_details VALUES (?, ?, ?, ?, ?)
        '''

        # executing script
        id = gen_id()
        data_tuple = (id, *data_tuple)
        cursor.execute(sql_script, data_tuple)
        self.conn.commit()

        # conceding cursor
        cursor.close()

        return id

    def delete(self, id: str):
        '''
        Deletes a record from shipment_details table

        Parameters
        ----------
        id: str
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        DELETE FROM shipment_details WHERE id = ?
        '''

        # executing script
        cursor.execute(sql_script, (id,))
        self.conn.commit()

        # conceding cursor
        cursor.close()

    def update(self, id: str, new_data: tuple):
        '''
        Updates a record of the shipment_details table using id

        Parameters
        ----------
        id: str
            id of the record in the db
        new_data: tuple
            tuple of new values (category, warehouse_id)
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        UPDATE shipment_details
        SET shipped_from = ? ,
            shipped_to = ? ,
            expected_shipping_date = ? ,
            shipping_time = ? 
        WHERE id=?
        '''

        # executing script
        new_data = (*new_data, id)
        cursor.execute(sql_script, new_data)
        self.conn.commit()

        # conceding cursor
        cursor.close()

    def getByID(self, id: str):
        '''
        gets a record from the shipment_details table using id

        Parameters
        ----------
        id: str
            id of the record in the db

        Returns
        -------
        query: tuple
            represents the result 
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        SELECT * FROM shipment_details WHERE id = ? 
        '''

        # executing script
        cursor.execute(sql_script, (id,))

        query = cursor.fetchone()

        # conceding cursor
        cursor.close()

        return query

    def getAll(self, order: str = 'DESC'):
        '''
        gets a record from the shipment_details table using id

        Parameters
        ----------
        order: str Default = 'DESC'
            arrangement of the returned query
            ASC: ascending order
            DESC: descending order

        Returns
        -------
        query: list
            results list
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = f'''
        SELECT * FROM shipment_details ORDER BY expected_shipping_date {order} 
        '''

        # executing script
        cursor.execute(sql_script)

        query = cursor.fetchall()

        # conceding cursor
        cursor.close()

        return query


class ShipmentModel(BaseModel):
    '''
    ORM for shipment table with the following structure

    NOTE: 
    must create shipment_details reference first

    shipment (
        id CHARACTER(10) NOT NULL PRIMARY KEY,
        name text NOT NULL,
        status Character(10) NOT NULL,
        shelfIndex Text NOT NULL,
        category TEXT NOT NULL,
        address Text NULL,
        shipper_vehicle_id NUMBER NULL,
        created_date TEXT NOT NULL,
        inventory CHARACTER(10) NOT NULL,
        shipment_details_id CHARACTER(10) NOT NULL
    );
    '''

    def __init__(self, db_filename: str):
        super(ShipmentModel, self).__init__(db_filename)
        self.shippment_data_model = _ShipmentDetailsModel(db_filename)

    def insert(self, data_tuple: tuple, shipment_details: tuple):
        '''
        Inserts a new record in shipment table

        Parameters
        ----------
        data_tuple: tuple
            tuple of shipping values in the form of 
            (name, status, shelfIndex, category, address,
                shipper_vehicle, created_date, 
                inventory_id)
        shipment_details: tuple 
            tuple of shipment details in the form 
            (shipped_from, shipped_to, expected_shipping_date, shipping_time)
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # inserting shipment details
        det_id = self.shippment_data_model.insert(shipment_details)

        # inserting shipment data
        # sql script
        sql_script = '''
        INSERT INTO shipment 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        # executing script
        id = gen_id()
        data_tuple = (id, *data_tuple, det_id)
        cursor.execute(sql_script, data_tuple)
        self.conn.commit()

        # conceding cursor
        cursor.close()

        return id

    def delete(self, id: str):
        '''
        Deletes a record from shipment table

        Parameters
        ----------
        id: str
        '''
        # aquiring cursor
        cursor = self.conn.cursor()
        self.conn.execute("PRAGMA foreign_keys = ON")

        # sql script
        sql_script = '''
        DELETE FROM shipment WHERE id = ?
        '''

        # executing script
        cursor.execute(sql_script, (id,))
        self.conn.commit()

        # conceding cursor
        cursor.close()

    def update(self, id: str, new_data: tuple, new_shipment_details: tuple):
        '''
        Updates a record of the shipment table using id

        Parameters
        ----------
        data_tuple: tuple
            tuple of shipping values in the form of 
            (name, status, shelfIndex, category, address,
                shipper_vehicle, created_date, 
                inventory_id)
        shipment_details: tuple 
            tuple of shipment details in the form 
            (shipped_from, shipped_to, expected_shipping_date, shipping_time)
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # delete old shipment details
        sql_script = '''
        DELETE FROM shipment_details
        WHERE id = EXISTS (
            SELECT shipment_details_id
            FROM shipment
            WHERE id=? 
            )
        '''
        cursor.execute(sql_script, (id,))
        self.conn.commit()

        # adding new data
        new_det_id = self.shippment_data_model.insert(new_shipment_details)
        # sql script
        sql_script = '''
        UPDATE shipment
        SET name = ? ,
            status = ?,
            shelfIndex = ?,
            category = ?,
            address = ?,
            shipper_vehicle_id = ?,
            created_date = ?,
            inventory_id = ?,
            shipment_details_id = ?
        WHERE id=?
        '''

        # executing script
        new_data = (*new_data, new_det_id, id)
        cursor.execute(sql_script, new_data)
        self.conn.commit()

        # conceding cursor
        cursor.close()

    def getByID(self, id: str):
        '''
        gets a record from the shipment table using id

        Parameters
        ----------
        id: str
            id of the record in the db

        Returns
        -------
        query: tuple
            represents the result 
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        SELECT * FROM shipment WHERE id = ? 
        '''

        # executing script
        cursor.execute(sql_script, (id,))

        query = cursor.fetchone()

        # conceding cursor
        cursor.close()

        return query

    def getAll(self, order: str = 'DESC'):
        '''
        gets a record from the shipment table using id

        Parameters
        ----------
        order: str Default = 'DESC'
            arrangement of the returned query
            ASC: ascending order
            DESC: descending order

        Returns
        -------
        query: list
            results list
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script to join between all tables
        sql_script = f'''
        SELECT 
            shipment.id,
            shipment.name,
            shipment.status,
            shipment.shelfIndex,
            shipment.category,
            shipment.address,
            shipment.shipper_vehicle_id,
            shipment.created_date,
            shipment_details.shipping_time,
            shipment_details.expected_shipping_date,
            shipment_details.shipped_from,
            shipment_details.shipped_to,
            inventory.name,
            warehouse.name
        FROM shipment JOIN shipment_details
        ON shipment.shipment_details_id = shipment_details.id
        JOIN inventory
        ON shipment.inventory_id = inventory.id
        JOIN warehouse
        ON inventory.warehouse_id = warehouse.id
        ORDER BY shipment.created_date {order} 
        '''

        # executing script
        cursor.execute(sql_script)

        query = cursor.fetchall()

        # conceding cursor
        cursor.close()

        return query

    def printALLDDs(self):
        print(self.shippment_data_model.getAll())
