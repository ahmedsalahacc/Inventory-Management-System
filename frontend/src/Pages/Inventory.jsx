import React, {useState, useEffect} from 'react'

import {Container, Row, Table, Button, Form} from  'react-bootstrap'

import {SERVER} from '../constants'

function Inventory() {
  const [data, setData] = useState([])

  useEffect(()=>{
    fetchDataToDisplay(setData)
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
                <th>Warehouse ID</th>
                <th>Desc</th>
                <th>Category</th>
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
                <td>{val[3]}</td>
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
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Invenotry Name</Form.Label>
              <Form.Control required name="name" type="text" placeholder="Inventory Name" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Warehouse ID</Form.Label>
              <Form.Control required name="warehouse_id" type="text" placeholder="Warehouse ID"/>
            </Form.Group>

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
  let category = target.category.value
  console.log(name, warehouseId,desc,category)

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
    fetchDataToDisplay(callback)
  })
}

function fetchDataToDisplay(callback){

  fetch(SERVER+'/inventory/all')
  .then(res=>res.json())
  .then((res)=>{
    callback(res.message)
    console.log(res)
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

//@TODO for the dropdown of the warehouses
function getAvailableInventories(){

}
export default Inventory