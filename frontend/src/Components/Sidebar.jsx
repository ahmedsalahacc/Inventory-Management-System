import React from 'react'
import {Link} from 'react-router-dom'

import '../css/sidebar.css'

function Sidebar() {
    return (
        <div className='sidebar'>
            <Link to='/'
            style={{
                color:"white",
                textDecoration:'none'
            }}
            >
                <h1 className='container mx-2 mb-4'>
                    Ship it
                </h1>
            </Link>
            <hr/>
            <Menu></Menu>
        </div>
    )
}

const  Menu= () => {
    return ( 
    <ul>

        <MenuItem content='Warehouses' to='/'/>
        <MenuItem content='Inventories' to='/inventories'/>
        <MenuItem content='Shipments' to='/shipments'/>

    </ul> 
    );
}
 
const MenuItem= ({content, to}) => {
    return (  <Link 
                style={{
                    color:'white',
                    textDecoration:"none",
                }} 
                to={to} 
                className='container mt-3'>
                 <h5>{content}</h5>
              </Link>
        );
}
 


export default Sidebar
