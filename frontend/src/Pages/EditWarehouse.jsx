import React, {useState, useEffect} from 'react'
import {useParams,} from 'react-router-dom'

import { SERVER } from '../constants'

import {Container, Row, Form, Button} from 'react-bootstrap'

function EditWarehouse() {
  const {id} = useParams()

  // default data state
  const [content, setContent] = useState([])

  // get default data
  useEffect(()=>{
    const abortController = new AbortController();
    const signal = abortController.signal

    fetchById(id, setContent, signal)

     return ()=>{
       // abort to clean up
       abortController.abort()
     }
  }, [])


  return (
    <div>
      <Container className="container__style">
        <Row>
          <h4>Edit Warehouse</h4>
          <Form onSubmit={(e)=>formSubmitHandler(e, id)}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Warehouse Name</Form.Label>
              <Form.Control required name="name" type="text" placeholder="Warehouse Name" defaultValue={content[1]} />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Location</Form.Label>
              <Form.Control required defaultValue={content[2]} name="location" type="text" placeholder="Location"/>
            </Form.Group>
            <Button variant="primary"  type="submit">
              Submit
            </Button>

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

  window.location.href = '/warehouses'
}

async function fetchById(id, callback, signal=null){
const URI = '/warehouse/'+id
  const URL = SERVER+URI

  await fetch(URL, {signal:signal})
  .then(res=>res.json())
  .then(res=>{
    callback(res.message)
  })
}
export default EditWarehouse