from models import BaseModel, gen_id


class WarehouseModel(BaseModel):
    '''
    ORM for Warehouse table with the following structure

    warehouse(
        id CHARACTER(10) NOT NULL PRIMARY KEY,
        name TEXT NOT NULL,
        location TEXT NOT NULL
    );
    '''

    def __init__(self, db_filename: str):
        super(WarehouseModel, self).__init__(db_filename)

    def insert(self, data_tuple: tuple):
        '''
        Inserts a new record in warehouse table

        Parameters
        ----------
        data_tuple: tuple
            tuple of values (name, location)
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        INSERT INTO warehouse VALUES (?, ?, ?)
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
        Deletes a record from warehouse table

        Parameters
        ----------
        id: str
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        DELETE FROM warehouse WHERE id = ?
        '''

        # executing script
        cursor.execute(sql_script, (id,))
        self.conn.commit()

        # conceding cursor
        cursor.close()

    def update(self, id: str, new_data: tuple):
        '''
        Updates a record of the warehouse table using id

        Parameters
        ----------
        id: str
            id of the record in the db
        data_tuple: tuple
            tuple of new values (name, location)
        '''
        # aquiring cursor
        cursor = self.conn.cursor()

        # sql script
        sql_script = '''
        UPDATE warehouse
        SET name = ? ,
            location = ?
        WHERE id = ?
        '''

        # executing script
        new_data = (*new_data, id)
        cursor.execute(sql_script, new_data)
        self.conn.commit()

        # conceding cursor
        cursor.close()

    def getByID(self, id: str):
        '''
        gets a record from the warehouse table using id

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
        SELECT * FROM warehouse WHERE id = ? 
        '''

        # executing script
        cursor.execute(sql_script, (id,))

        query = cursor.fetchone()

        # conceding cursor
        cursor.close()

        return query

    def getAll(self, order: str = 'ASC'):
        '''
        gets a record from the warehouse table using id

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
        SELECT * FROM warehouse ORDER BY name {order} 
        '''

        # executing script
        cursor.execute(sql_script)

        query = cursor.fetchall()

        # conceding cursor
        cursor.close()

        return query
