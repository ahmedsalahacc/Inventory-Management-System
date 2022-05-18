import React, {useState, useEffect}from 'react'
import { useParams } from 'react-router-dom'

import {Container, Row, Col, Table, Button, Form} from 'react-bootstrap'

import {SERVER} from '../constants'

function EditShipment() {
  const [data, setData] = useState([])
  const [inventories, setInventories] = useState([])
  const [content, setContent] = useState([])
  const {id} = useParams()

  useEffect(()=>{
    const abortController = new AbortController();
    const signal = abortController.signal;

    fetchAvailableInventories(setInventories, signal)
    getShipmentById(id, setContent, signal)

    return ()=>{
      abortController.abort()
    }
  }, [])

  return (
    <div>
      <Container className="container__style">
        <Row>
          <h4>Edit Shipment</h4>
          <Form onSubmit={(e)=>formSubmitHandler(e, id)}>
            <Row>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Shipment's Name*</Form.Label>
                  <Form.Control defaultValue={content[1]} name="name" type="text" placeholder="Shipment's Name" />
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Category*</Form.Label>
                  <Form.Control defaultValue={content[4]} required name="category" type="text" placeholder="Category"/>
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Shelf Index*</Form.Label>
                  <Form.Control defaultValue={content[3]} required name="shelfIndex" type="text" placeholder="Shelf Index"/>
                </Form.Group>
              </Col>
            </Row>
            <Row>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Shipper Vehicle</Form.Label>
                  <Form.Control defaultValue={content[6]} name="shipperVehicle" type="text" placeholder="Shipper Vehicle" />
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Sender's Name*</Form.Label>
                  <Form.Control defaultValue={content[10]} required name="shippedFrom" type="text" placeholder="Shipped From"/>
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Reciever's Name*</Form.Label>
                  <Form.Control defaultValue={content[11]} required name="shippedTo" type="text" placeholder="Shipped To"/>
                </Form.Group>
              </Col>
            </Row>
            <Row>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Shipping Date*</Form.Label>
                  <Form.Control defaultValue={content[7]} required name="shippingDate" type="date" placeholder="Shipping Date"/>
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Shipping Time</Form.Label>
                  <Form.Control defaultValue={content[8]} name="shippingTime" type="time" placeholder="Shipping Time"/>
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
                <Form.Control defaultValue={content[5]} required name="address" type="text" placeholder="Address"/>
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

async function formSubmitHandler(e, id){
  e.preventDefault()

  // extract data
  let target = e.target;
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
  await fetch(SERVER+'/shipment/'+id,
    {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "PUT",
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
  ).catch(e=>alert(e))

  window.location.href = '/shipments'

}

async function fetchAvailableInventories(callback, signal=null){
  await fetch(SERVER+'/inventory/all', {signal:signal})
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
  }).catch(e=>alert(e))
}

async function getShipmentById(id, callback, signal=null){
 await fetch(SERVER+'/shipment/'+id, {signal:signal})
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
    console.log(res.message)
  }).catch(e=>alert(e))
}

export default EditShipment