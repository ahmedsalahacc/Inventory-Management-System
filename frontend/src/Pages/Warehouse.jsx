import React, { useEffect, useState } from 'react'

import {Col, Row, Container, Table, Form, Button} from 'react-bootstrap'

import './styles/warehouse.css'

import {SERVER} from '../constants'

function Warehouse() {
  const [data, setData] = useState([])

  useEffect(()=>{
    fetchDataToDisplay(setData)
  }, [])
  return (
    <div>
      <Container className="container__style">
        <h1>Warehouses</h1>
        <Row className="table__style">
          <Table striped bordered hover variant="dark">
            <thead style={{
              position: 'sticky',
              top: 0
            }}>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Location</th>
                <th>Operations</th>
              </tr>
            </thead>
            <tbody  >
              {
                data.map((val, idx)=>{
                  return (<tr>
                <td key={idx}>{val[0]}</td>
                <td key={idx+100}>{val[1]}</td>
                <td key={idx+200}>{val[2]}</td>
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
        <Row>
          <h4>Enter a New Warehouse</h4>
          <Form onSubmit={(e)=>formSubmitHandler(e, setData)}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Warehouse Name</Form.Label>
              <Form.Control required name="name" type="text" placeholder="Warehouse Name" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Location</Form.Label>
              <Form.Control required name="location" type="text" placeholder="Location"/>
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
  let location = target.location.value
  console.log(name, location)

  //post request to add data
  fetch(SERVER+'/warehouse',
    {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({'name': name, 'location': location})
    }
  ).then(_=>{
    fetchDataToDisplay(callback)
  })
}

function fetchDataToDisplay(callback){

  fetch(SERVER+'/warehouse/all')
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
    console.log(res)
  })
}

function deleteDataItem(id, callback){
  fetch(SERVER+'/warehouse/'+id.toString(),
  {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "DELETE",
    })
  .then(res=>res.json())
  .then((res)=>{
    fetchDataToDisplay(callback)
  })
}
export default Warehouse