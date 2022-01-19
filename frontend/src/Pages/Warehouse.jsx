import React from 'react'
import { Alert, AlertTitle } from '@mui/material';

import WarehouseForm from '../Components/WarehouseForm';
import Table from '../Components/Table'

function Warehouse() {
    return (
        <div style={{
            transform:'translate(20%, 1%)',
            color:"black",
            marginBottom:"3%"
        }}>
            <div className="container">
               <Alert style={{
                   width:'80%'
               }} severity="info">
                <AlertTitle>No warehouses to show</AlertTitle>
                Add a new warehouse using the form below 👇
                </Alert>
            </div>
            <Table/>
            <WarehouseForm/>

        </div>
    )
}

export default Warehouse
