import React, {useState, useEffect} from 'react'
import {Container, Row, Table, Button, Form, Col} from 'react-bootstrap'

import {SERVER} from '../constants'

function Shipment() {
  const [data, setData] = useState([])
  const [inventories, setInventories] = useState([])

  useEffect(()=>{
    const abortController = new AbortController();
    const signal = abortController.signal;

    fetchDataToDisplay(setData, signal);
    fetchAvailableInventories(setInventories, signal)

    return ()=>{
      abortController.abort()
    }
  }, [])
  return (
    <div>
      <Container className="container__style">
        <h1>Shipments</h1>
        <Row className="table__style">
          <Table striped bordered hover variant="dark">
            <thead style={{
              position: 'sticky',
              top: 0
            }}>
              <tr>
                <th>ID</th>
                <th>Product's Name</th>
                <th>Status</th>
                <th>Shelf Index</th>
                <th>Category</th>
                <th>Reciever's Address</th>
                <th>Shipper Vehicle</th>
                <th>Date Created</th>
                <th>Shipping Date</th>
                <th>Shipping Time</th>
                <th>Sender's Name</th>
                <th>Reciever's Name</th>
                <th>Inventory's Name</th>
                <th>Warehouse's Name</th>
                <th>Operations</th>
              </tr>
            </thead>
            <tbody  >
              {
                data.map((val, idx)=>{
                  return (<tr key={val[0]}>
                <td>{val[0]}</td>
                <td>{val[1]}</td>
                <td>{val[2]}</td>
                <td>{val[3]}</td>
                <td>{val[4]}</td>
                <td>{val[5]}</td>
                <td>{val[6]}</td>
                <td>{val[7]}</td>
                <td>{val[9]}</td>
                <td>{val[8]}</td>
                <td>{val[10]}</td>
                <td>{val[11]}</td>
                <td>{val[12]}</td>
                <td>{val[13]}</td>
                <td >
                  <Button className='table__btn' size='sm' variant="info">Edit</Button> 
                  <Button className='table__btn' size='sm' onClick={(e)=>{deleteDataItem(val[0], setData)}} variant="danger">Delete</Button>
                </td>
              </tr>);
                })
              }
            </tbody>
        </Table>
        </Row>
        <br />
        <Row>
          <h4>Enter a New Shipment</h4>
          <Form onSubmit={(e)=>formSubmitHandler(e, setData)}>
            <Row>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Shipment's Name*</Form.Label>
                  <Form.Control name="name" type="text" placeholder="Shipment's Name" />
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Category*</Form.Label>
                  <Form.Control required name="category" type="text" placeholder="Category"/>
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Shelf Index*</Form.Label>
                  <Form.Control required name="shelfIndex" type="text" placeholder="Shelf Index"/>
                </Form.Group>
              </Col>
            </Row>
            <Row>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Shipper Vehicle</Form.Label>
                  <Form.Control name="shipperVehicle" type="text" placeholder="Shipper Vehicle" />
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Sender's Name*</Form.Label>
                  <Form.Control required name="shippedFrom" type="text" placeholder="Shipped From"/>
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Reciever's Name*</Form.Label>
                  <Form.Control required name="shippedTo" type="text" placeholder="Shipped To"/>
                </Form.Group>
              </Col>
            </Row>
            <Row>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Shipping Date*</Form.Label>
                  <Form.Control required name="shippingDate" type="date" placeholder="Shipping Date"/>
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Shipping Time</Form.Label>
                  <Form.Control  name="shippingTime" type="time" placeholder="Shipping Time"/>
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Status*</Form.Label>
                  <Form.Select required name="status" aria-label="Default select example">
                    <option key={0} value='unspecified'>select a status...</option>
                    <option key={1} value='new'>New</option>
                    <option key={2} value='preparing'>Preparing</option>
                    <option key={3} value='shipping'>Shipping</option>
                    <option key={4} value='arrived'>Arrived</option>
                    <option key={5} value='cancelled'>Cancelled</option>
                  </Form.Select>
                </Form.Group>
              </Col>
            </Row>
            <Row>
              <Col>
                <Form.Label>Address*</Form.Label>
                <Form.Control required name="address" type="text" placeholder="Address"/>
              </Col>
              <Col>
                  <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Select an Inventory*</Form.Label>
                  <Form.Select required name="inventory" aria-label="Default select example">
                    <option key={0} value='unspecified'>select an inventory...</option>
                    {
                      inventories.map((value)=>{
                        return (
                          <option key={value[0]} value={value[0]}>{value[1]}</option>
                        )
                      })
                    }
                  </Form.Select>
                </Form.Group>
              </Col>
            </Row>
            <Button variant="primary"  type="submit">
              Add
            </Button>
          </Form>
        </Row>
      </Container>
    </div>
  )

}

function formSubmitHandler(e, callback){
  e.preventDefault()

  // extract data
  let target = e.target;
  console.log(target.status.value)
  let name = target.name.value
  let shelfIndex = target.shelfIndex.value
  let category = target.category.value
  let status = target.status.value
  let shipperVehicle = target.shipperVehicle.value
  let shippedFrom = target.shippedFrom.value
  let shippedTo = target.shippedTo.value
  let shippingDate = target.shippingDate.value
  let shippingTime = target.shippingTime.value
  let address = target.address.value
  let inventory = target.inventory.value
  
  if (inventory === 'unspecified'){
    alert("Please select an inventory")
    return
  }
  if (status === 'unspecified'){
    alert("Please select a status")
    return
  }

  //post request to add data
  fetch(SERVER+'/shipment',
    {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({
      name: name,
      shelfIndex:shelfIndex,
      category:category,
      status:status,
      shipperVehicle:shipperVehicle,
      shippedFrom: shippedFrom, 
      shippedTo:shippedTo,
      shippingDate:shippingDate,
      shippingTime:shippingTime,
      address:address,
      inventory:inventory
    })
    }
  ).then(_=>{
    fetchDataToDisplay(callback)
  })
}

function fetchDataToDisplay(callback, signal=null){

  fetch(SERVER+'/shipment/all', {signal:signal})
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
  })
}

function deleteDataItem(id, callback){
  fetch(SERVER+'/shipment/'+id.toString(),
  {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "DELETE",
    })
  .then(res=>res.json())
  .then((_)=>{
    fetchDataToDisplay(callback)
  })
}

//@TODO for the dropdown of the warehouses
function fetchAvailableInventories(callback, signal=null){
  fetch(SERVER+'/inventory/all', {signal:signal})
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
  })
}

export default Shipment