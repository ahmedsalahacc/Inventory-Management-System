import React from 'react'
import { Alert, AlertTitle, TextField } from '@mui/material';
import { Container} from '@mui/material';
import { Field } from '@mui/material';

import ShipmentForm from '../Components/ShipmentForm'
import Table from '../Components/Table'

function Shipments() {
    return (
        <div style={{
            transform:'translate(20%, 1%)',
            color:"black",
            overflowY:"scroll",
            overflowX:"hidden",
        }}>
            <div className="container">
               <Alert style={{
                   width:'80%'
               }}severity="info">
                <AlertTitle>No shipments to show</AlertTitle>
                Add a new shipment using the form below 👇
                </Alert>
            </div>
            <Table/>
            <ShipmentForm/>
           <br/>
        </div>
    )
}

export default Shipments
