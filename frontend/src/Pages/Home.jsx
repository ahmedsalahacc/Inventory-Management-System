import React from 'react'

import {Container, Accordion} from 'react-bootstrap'

function Home() {
  return (
    <div>
        <Container>
            <h1>Welcome to <strong>Manageeto</strong></h1>
            <br />
            <br />
            <div className="container" style={{width: '40%'}}>
            <h3>How to use?</h3>
            <Accordion defaultActiveKey="0">
                <Accordion.Item eventKey="0">
                    <Accordion.Header >
                        What is Manageeto? 
                    </Accordion.Header>
                        <Accordion.Body>
                            <p style={{textAlign:'left'}}>
                                Manageeto is an inventory management system to simplify the lives of logistics companies by digitalizing the
                                process.
                            </p>
                        </Accordion.Body>
                </Accordion.Item>
                <Accordion.Item eventKey="1">
                    <Accordion.Header>Warehouses</Accordion.Header>
                    <Accordion.Body>
                    <p style={{textAlign:'left'}}>
                        To <strong>add</strong> a new warehouse, all you have to do is to go to the warehouses page by pressing the
                        "Warehouses" icon in the navbar. You will find a form that takes the "name" and "location" of the warehouse, press 
                        submit to add the entery to the database and VOLA, the table will update  and <strong>view</strong> all existing warehouses and you will find your 
                        warehouse in the table.

                    </p>
                        
                    <p style={{textAlign:'left'}}>
                        To <strong>delete</strong> a warehouse, all what you have to do is to press the delete button in the operations column of the corresponding warehouse
                        which you want to delete. 
                    </p>

                    <p style={{textAlign:'left'}}>
                        To <strong>update</strong>  warehouse's details, all what you have to do is to press the edit button in the operations column of the corresponding warehouse 
                        which will take you to another page where you can update the details of the corresponding warehouse.
                    </p>
                    </Accordion.Body>
                </Accordion.Item>
                <Accordion.Item eventKey="2">
                    <Accordion.Header>Inventories</Accordion.Header>
                    <Accordion.Body>
                     <p style={{textAlign:'left'}}>
                        To <strong>add</strong> a new inventory, all you have to do is to go to the inventories page by pressing the
                        "inventories" icon in the navbar. You will find a form that takes the "name" and "location" of the inventory, press 
                        submit to add the entery to the database and VOLA, the table will update  and <strong>view</strong> all existing inventories and you will find your 
                        inventory in the table.

                    </p>
                    <p style={{textAlign:'left'}}>
                        <strong>NOTE THAT:</strong> You must select an existing warehouse to be associated with the inventory that you wish to add
                    </p>
                    <p style={{textAlign:'left'}}>
                        To <strong>delete</strong> an inventory, all what you have to do is to press the delete button in the operations column of the corresponding inventory
                        which you want to delete. 
                    </p>

                    <p style={{textAlign:'left'}}>
                        To <strong>update</strong>  inventory's details, all what you have to do is to press the edit button in the operations column of the corresponding inventory 
                        which will take you to another page where you can update the details of the corresponding inventory.
                    </p>
                    </Accordion.Body>
                </Accordion.Item>
                <Accordion.Item eventKey="3">
                    <Accordion.Header>Shipments</Accordion.Header>
                    <Accordion.Body>
                    <p style={{textAlign:'left'}}>
                        To <strong>add</strong> a new shipment, all you have to do is to go to the shipments page by pressing the
                        "shipments" icon in the navbar. You will find a form that takes the "name" and "location" of the shipment, press 
                        submit to add the entery to the database and VOLA, the table will update and <strong>view</strong> all existing shipments and you will find your 
                        shipment in the table.

                    </p>
                    <p style={{textAlign:'left'}}>
                        <strong>NOTE THAT:</strong> You must select an existing inventory to be associated with the shipment that you wish to add
                    </p>
                    <p style={{textAlign:'left'}}>
                        To <strong>delete</strong> a shipment, all what you have to do is to press the delete button in the operations column of the corresponding shipment
                        which you want to delete. 
                    </p>

                    <p style={{textAlign:'left'}}>
                        To <strong>update</strong> shipment's details, all what you have to do is to press the edit button in the operations column of the corresponding shipment 
                        which will take you to another page where you can update the details of the corresponding shipment.
                    </p>
                    </Accordion.Body>
                </Accordion.Item>
            </Accordion>
            </div>
        </Container>
    </div>
  )
}

export default Home