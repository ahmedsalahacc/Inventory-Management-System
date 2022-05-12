from models import BaseModel, gen_id


class InventoryModel(BaseModel):
    '''
    ORM for Inventory table with the following structure

    inventory(
       id CHARACTER(10) NOT NULL PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        desc TEXT NULL,
        warehouse_id CHARACTER(10) NULL,
    )
    '''

    def __init__(self, db_filename: str):
        super(InventoryModel, self).__init__(db_filename)

    def insert(self, data_tuple: tuple):
        '''
        Inserts a new record in inventory table

        Parameters
        ----------
        data_tuple: tuple
            tuple of new values (name, category, desc, warehouse_id)
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        INSERT INTO inventory VALUES (?, ?, ?, ?, ?)
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
        Deletes a record from inventory table

        Parameters
        ----------
        id: str
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        DELETE FROM inventory WHERE id = ?
        '''

        # executing script
        cursor.execute(sql_script, (id,))
        self.conn.commit()

        # conceding cursor
        cursor.close()

    def update(self, id: str, new_data: tuple):
        '''
        Updates a record of the inventory table using id

        Parameters
        ----------
        id: str
            id of the record in the db
        new_data: tuple
            tuple of new values (name, category, desc, warehouse_id)
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        UPDATE inventory
        SET name = ?,
            category = ?,     
            desc = ?,
            warehouse_id = ? 
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
        gets a record from the inventory table using id

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
        SELECT inventory.id, inventory.name, inventory.category,
            inventory.desc, inventory.warehouse_id,
            warehouse.name, warehouse.location
        FROM inventory JOIN warehouse
        ON inventory.warehouse_id = warehouse.id
        WHERE inventory.id = ?
        '''

        # executing script
        cursor.execute(sql_script, (id,))

        query = cursor.fetchone()

        # conceding cursor
        cursor.close()

        return query

    def getAll(self, order: str = 'ASC'):
        '''
        gets a record from the inventory table using id

        Parameters
        ----------
        order: str Default = 'asc'
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
        SELECT inventory.id, inventory.name, inventory.category,
            inventory.desc, inventory.warehouse_id,
            warehouse.name
        FROM inventory JOIN warehouse
        ON inventory.warehouse_id = warehouse.id
        ORDER BY category {order} 
        '''

        # executing script
        cursor.execute(sql_script)

        query = cursor.fetchall()

        # conceding cursor
        cursor.close()

        return query
