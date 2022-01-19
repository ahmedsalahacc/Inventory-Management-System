import React from 'react'
import { Alert, AlertTitle } from '@mui/material';

import ShipmentForm from '../Components/WarehouseForm'
import WarehouseForm from '../Components/WarehouseForm';


function Warehouse() {
    return (
        <div style={{
            transform:'translate(20%, 1%)',
            color:"black"
        }}>
            <div className="container">
               <Alert style={{
                   width:'80%'
               }} severity="info">
                <AlertTitle>No warehouses to show</AlertTitle>
                Add a new warehouse using the form below 👇
                </Alert>
            </div>
            <WarehouseForm/>

        </div>
    )
}

export default Warehouse
