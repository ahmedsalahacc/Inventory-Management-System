from models.Inventory import InventoryModel
from models.Warehouse import WarehouseModel
from environment.config import config

# seeding items into the database
DB_FILEPATH = config['DB']['DB_FILEPATH']

# @TODO seed warehouse data


def seedWarehouseData():
    '''
    seeds warehouse data into the database
    '''
    whDB = WarehouseModel(DB_FILEPATH)

    # whDB.insert(('WH1', '6th october'))

    print("inserted to db")

    vals = whDB.getAll()
    print("retrieved from db")
    print(vals)

    query = whDB.getByID('d92e8632-7')
    print(query)

    whDB.update('e89c8384-5', ('WH2', 'Nasr City'))


# @TODO seed inventory data

def seedInventoryData():
    '''
    seeds inventory data into the database
    '''
    invDB = InventoryModel(DB_FILEPATH)

    # inserting into the database
    invDB.insert(('Electronics', 'e89c8384-5'))

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
    pass
