from models.Inventory import InventoryModel
from models.Warehouse import WarehouseModel
from models.Shipment import ShipmentModel

from environment.config import config

# seeding items into the database
DB_FILEPATH = config['DB']['DB_FILEPATH']

# @TODO seed warehouse data


def seedWarehouseData():
    '''
    seeds warehouse data into the database
    '''
    whDB = WarehouseModel(DB_FILEPATH)

    whDB.insert(('WH1', '6th october'))

    print("inserted to db")

    vals = whDB.getAll()
    print("retrieved from db")
    print(vals)


# @TODO seed inventory data

def seedInventoryData():
    '''
    seeds inventory data into the database
    '''
    invDB = InventoryModel(DB_FILEPATH)

    # inserting into the database
    invDB.insert(('AAA01', 'Electronics', 'desc', 'e89c8384-5'))

    # retrieving from db
    queries = invDB.getAll()
    print(queries)

    # updating record
    invDB.update('2d87d8b2-7', ('Mobiles', 'e89c8384-5'))

    # delete record
    invDB.delete('2d87d8b2-7')

    # get one
    query = invDB.getByID('f6f17c3a-5')
    print(query)

# @TODO seed shipment data


def seedShipmentData():
    '''seeds shipment data into database'''
    shDB = ShipmentModel(DB_FILEPATH)
    # seed shipment
    # insert
    data1 = ('hello', 'hello', 'hello', 'hello', 'hello',
             69, '2022-07-02', '2022-07-12', '8ba0bf39-5')
    datash1 = ('Ahmed Salah', 'Ahmed Salah', '2022-07-12')
    shDB.insert(data1, datash1)
    print("Inserted shipment details")
    # retrieve
    query = shDB.getAll()
    print('Query', query)
    # delete
    print("deleting")
    shDB.delete('a175e9e4-1')
    print(query)
    # update
    print("updating")
    new_data = ('samy', 'SALALALAAL', 'Ahmed', 'Salah', 'hello',
                69, '2022-07-02', '2022-07-12', '8db71e96-a')
    datash1 = ('Ahmed Salah', 'Ahmed Salah Keda Keda', '2022-07-14')
    shDB.update('3f4b94c1-9', new_data, datash1)
    query = shDB.getAll()
    print(query)
    print("------------")
    print('DDs')
    print(shDB.printALLDDs())
    #-- sh2
    #-- sh3
    #-- sh4
