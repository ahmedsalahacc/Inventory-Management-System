import React, {useState, useEffect} from 'react'

import { SERVER } from '../constants'

import { Container, Row, Button, Form, Col } from 'react-bootstrap'

function EditInventory() {

  const [warehouses, setWarehouses] = useState([])

  useEffect(()=>{
    const abortController = new AbortController();
    const signal = abortController.signal;

    // fetchDataToDisplay(setData, signal);
    fetchAvailableWarehouses(setWarehouses, signal)

    return ()=>{
      abortController.abort()
    }
  }, [])
  return (
    <Container classname="container__style">
      <h4>Enter a New Inventory</h4>
      <Row>
          <Form onSubmit={(e)=>formSubmitHandler(e)}>
            <Row>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Inventory Name</Form.Label>
                  <Form.Control required name="name" type="text" placeholder="Inventory Name" />
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Select a Warehouse</Form.Label>
                  <Form.Select name="warehouse_id" aria-label="Default select example">
                    <option value='unspecified'>select a warehouse...</option>
                    {
                      warehouses.map((value)=>{
                        return (
                          <option value={value[0]}>{value[1]}</option>
                        )
                      })
                    }
                  </Form.Select>
                </Form.Group>
              </Col>
            </Row>
            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Description</Form.Label>
              <Form.Control required name="desc" type="text" placeholder="Description"/>
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Category</Form.Label>
              <Form.Control required name="category" type="text" placeholder="Category"/>
            </Form.Group>
            <Button variant="primary"  type="submit">
              Add
            </Button>
          </Form>
        </Row>
    </Container>
  )
}

function formSubmitHandler(e, callback){
  e.preventDefault()

  // extract data
  let target = e.target;
  let name = target.name.value
  let warehouseId = target.warehouse_id.value
  let desc = target.desc.value
  let category = target.category.value
  
  if (warehouseId === 'unspecified'){
    alert("Please select a warehouse")
    return
  }

  //post request to add data
  fetch(SERVER+'/inventory',
    {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({
      'name': name,
      'warehouse_id': warehouseId,
      'desc':desc,
      'category': category
    })
    }
  ).then(_=>{
    // fetchDataToDisplay(callback)
  })
}

function fetchAvailableWarehouses(callback, signal=null){
  fetch(SERVER+'/warehouse/all', {signal:signal})
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
  })
}
export default EditInventory