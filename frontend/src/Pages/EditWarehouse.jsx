import React from 'react'
import {useParams} from 'react-router-dom'

import { SERVER } from '../constants'

import {Container, Row, Button, Form} from 'react-bootstrap'

function EditWarehouse() {
  const {id} = useParams()
  return (
    <div>
      <Container className="container__style">
        <Row>
          <h4>Edit Warehouse</h4>
          <Form onSubmit={(e)=>formSubmitHandler(e, id)}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Warehouse Name</Form.Label>
              <Form.Control required name="name" type="text" placeholder="Warehouse Name" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Location</Form.Label>
              <Form.Control required name="location" type="text" placeholder="Location"/>
            </Form.Group>
            <a className="btn btn-primary" href="/warehouses" variant="primary"  type="submit">
              Add
            </a>
          </Form>
        </Row>
      </Container>
    </div>
  )
}

function formSubmitHandler(e, id){
  e.preventDefault()

  // extract data
  let target = e.target;
  let name = target.name.value
  let location = target.location.value

  //post request to add data
  fetch(SERVER+'/warehouse/'+id,
    {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "PUT",
    body: JSON.stringify({'name': name, 'location': location})
    }
  )
}

//@TODO fetchById function
export default EditWarehouse