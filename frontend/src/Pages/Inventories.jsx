import React from 'react'
import { Alert, AlertTitle } from '@mui/material';

import InventoryForm from '../Components/InventoryForm';
import Table from '../Components/Table';


function Inventories() {
   return (
        <div style={{
            transform:'translate(20%, 1%)',
            color:"black"
        }}>
            <div className="container">
               <Alert style={{
                   width:'80%'
               }} severity="info">
                <AlertTitle>No inventories to show</AlertTitle>
                Add a new inventory using the form below 👇
                </Alert>
            </div>
            <Table/>
            <InventoryForm/>
            <br/>

        </div>
    )
}

export default Inventories
