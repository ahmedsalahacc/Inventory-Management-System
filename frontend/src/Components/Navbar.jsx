import React, {useState} from 'react'

import { Button, Offcanvas } from 'react-bootstrap';
import './styles/Navbar.css'


function Navbar() {
  const [show, setShow] = useState(true);
  const [btnColor, setBtnColor] = useState('white')

  const handleShow = () =>{
    setShow(!show)
    if(show===true) setBtnColor('black') 
    else setBtnColor('white')
    
  };

  return (
    <div className='__hamburger__div__component'>
      <Button variant="primary" 
        onClick={handleShow} 
        className="hamburger__btn"
        style={{
          color:`${btnColor}`
        }}
        >
         ≡
      </Button>

      <Offcanvas 
        show={show} 
        onHide='' 
        scroll={true} 
        backdrop={false}
        className="navbar"
      >
        <Offcanvas.Header>
            <Offcanvas.Title className="navbar__title">Manageeto Logistics System</Offcanvas.Title>

        </Offcanvas.Header>
        <Offcanvas.Body className="navbar__body">
         <ul className="navbar__items">
           <li><a href="/warehouses">Warehouses</a></li>
           <li><a href="/inventories">Inventories</a></li>
           <li><a href="/shipments">Shipments</a></li>
         </ul>
        </Offcanvas.Body>
      </Offcanvas>
    </div>
  );
}

export default Navbar