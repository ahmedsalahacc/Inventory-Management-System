import React, {useState, useEffect} from 'react'

import {Container, Row, Table, Button, Form, Col, Dropdown} from  'react-bootstrap'

import {SERVER} from '../constants'

function Inventory() {
  const [data, setData] = useState([])
  const [warehouses, setWarehouses] = useState([])

  useEffect(()=>{
    const abortController = new AbortController();
    const signal = abortController.signal;

    fetchDataToDisplay(setData, signal);
    fetchAvailableWarehouses(setWarehouses, signal)

    return ()=>{
      abortController.abort()
    }
  }, [])
  return (
    <div>
      <Container className="container__style">
        <h1>Inventories</h1>
        <Row className="table__style">
          <Table striped bordered hover variant="dark">
            <thead style={{
              position: 'sticky',
              top: 0
            }}>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Warehouse</th>
                <th>Desc</th>
                <th>Operations</th>
              </tr>
            </thead>
            <tbody  >
              {
                data.map((val, idx)=>{
                  return (<tr>
                <td>{val[0]}</td>
                <td>{val[1]}</td>
                <td>{val[4]}</td>
                <td>{val[2]}</td>
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
          <h4>Enter a New Inventory</h4>
          <Form onSubmit={(e)=>formSubmitHandler(e, setData)}>
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
  let name = target.name.value
  let warehouseId = target.warehouse_id.value
  let desc = target.desc.value
  
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
    })
    }
  ).then(_=>{
    fetchDataToDisplay(callback)
  })
}

function fetchDataToDisplay(callback, signal=null){

  fetch(SERVER+'/inventory/all', {signal:signal})
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
  })
}

function deleteDataItem(id, callback){
  fetch(SERVER+'/inventory/'+id.toString(),
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

function fetchAvailableWarehouses(callback, signal=null){
  fetch(SERVER+'/warehouse/all', {signal:signal})
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
  })
}
export default Inventory