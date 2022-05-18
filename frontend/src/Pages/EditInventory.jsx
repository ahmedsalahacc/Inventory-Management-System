import React, {useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'

import { SERVER } from '../constants'

import { Container, Row, Button, Form, Col } from 'react-bootstrap'

function EditInventory() {

  const [warehouses, setWarehouses] = useState([])
  const [content, setContent] = useState([])

  const {id} = useParams()

  useEffect(()=>{
      const abortController = new  AbortController()
      const signal = abortController.signal;

      fetchInventoryById(id, setContent, signal)

      return ()=>{
          // cleaning up
          abortController.abort()
      }
  }, [])

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
    <div>
    <Container className="container__style">
      <h4>Edit Inventory</h4>
      <Row>
          <Form onSubmit={(e)=>formSubmitHandler(e, id)}>
            <Row>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                  <Form.Label>Inventory Name</Form.Label>
                  <Form.Control defaultValue={content[1]} required name="name" type="text" placeholder="Inventory Name" />
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="mb-3" controlId="formBasicPassword">
                  <Form.Label>Select a Warehouse</Form.Label>
                  <Form.Select defaultValue={content[2]} name="warehouse_id" aria-label="Default select example">
                    <option key={0} value='unspecified'>select a warehouse...</option>
                    {
                      warehouses.map((value)=>{
                        return (
                          <option key={value[0]} value={value[0]}>{value[1]}</option>
                        )
                      })
                    }
                  </Form.Select>
                </Form.Group>
              </Col>
            </Row>
            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Description</Form.Label>
              <Form.Control defaultValue={content[2]} required name="desc" type="text" placeholder="Description"/>
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

async function formSubmitHandler(e, id){
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

  //PUT request to edit data
   await fetch(SERVER+'/inventory/'+id,
    {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "PUT",
    body: JSON.stringify({
      'name': name,
      'warehouse_id': warehouseId,
      'desc':desc,
    })
    }
  )

  window.location.href = '/inventories'

}

function fetchAvailableWarehouses(callback, signal=null){
  fetch(SERVER+'/warehouse/all', {signal:signal})
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
  })
}

async function fetchInventoryById(id, callback, signal=null){
    const URI = '/inventory/'+id
    const URL = SERVER+URI

    await fetch(URL, {signal:signal})
    .then(res=>res.json())
    .then(res=>
        callback(res.message)
    )
}
export default EditInventory