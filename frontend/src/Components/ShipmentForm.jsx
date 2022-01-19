
const ShipmentForm =()=>{
    return(
        <div className="container">
        <form style={{
            width:"50%",
            marginTop:"2%",
            marginLeft:"10%",
            
        }}>
            <fieldset>
                <legend>Add Shipment</legend>
                <div class="mb-3">
                    <div className="row">
                        <div className="col-lg-6">
                            <label for="disabledTextInput" class="form-label">Shipment Name<sup>*</sup></label>
                            <input type="text" id="disabledTextInput" class="form-control" placeholder="Shipment Name" required />
                        </div>
                        <div className="col-lg-6">
                            <label for="disabledTextInput" class="form-label">Shipment Status<sup>*</sup></label>
                            <select id="disabledSelect" class="form-select" required>
                                 <option>Select Status</option>
                                 <option>Waiting to be shipped</option>
                                 <option>Shipping</option>
                                 <option>Arrived</option>
                            </select>
                        </div>
                    </div>
                
                </div>
                <div class="mb-3">
                    <div className="row">
                        
                        <div className="col-lg-3">
                            <label for="disabledTextInput" class="form-label">Category<sup>*</sup></label>
                            <select id="disabledSelect" class="form-select" required>
                                 <option>Category</option>
                                 <option>Electronics</option>
                                 <option>Video Games</option>
                                 <option>Fashion</option>
                                 <option>Fragile</option>
                            </select>
                        </div>
                        <div className="col-lg-3">
                             <label for="disabledTextInput" class="form-label">Date to ship<sup>*</sup></label>
                            <input type="date" id="disabledTextInput" class="form-control" placeholder="" required />
                        </div>
                        <div className="col">
                             <label for="disabledTextInput" class="form-label">Inventory<sup>*</sup></label>
                            <select id="disabledSelect" class="form-select" required>
                                 <option>Inventory</option>
                            </select>
                        </div>
                        <div className="col-lg-3">
                            <label for="disabledTextInput" class="form-label">Shelf-Index <sup>*</sup></label>
                            <input type="number" id="disabledTextInput" class="form-control" placeholder="i.e. 10" min={0} max={200}/>
                             <div id="emailHelp" class="form-text">Range [0, 200]</div>
                        </div>
                    </div>
                    
                </div>
                <div class="mb-2">
                    <div className="row">
                        <div className="col-lg-6">
                            <label for="disabledTextInput" class="form-label">Address<sup>*</sup></label>
                            <input type="number" id="disabledTextInput" class="form-control" placeholder="Address"/>
                        </div>
                        <div className="col-lg-6">
                            <label for="disabledTextInput" class="form-label">Vehcile ID</label>
                            <input type="number" id="disabledTextInput" class="form-control" placeholder="Vehicle ID"/>
                            <div id="emailHelp" class="form-text">Optional if not decided</div>
                        </div>
                        
                    </div>
                </div>
                <div class="mb-2">
                    <div className="row">
                        <div className="col">
                            <label for="disabledTextInput" class="form-label">Shipped From<sup>*</sup></label>
                            <input type="number" id="disabledTextInput" class="form-control" placeholder="i.e. ALexis for glasses"/>
                        </div>
                        <div className="col">
                             <label for="disabledTextInput" class="form-label">Shipped To<sup>*</sup></label>
                            <input type="number" id="disabledTextInput" class="form-control" placeholder="Yann Lecun"/>
                        </div>
                    </div>
                </div>
                <div className="mb-2 mt-3">
                <button type="submit" class="btn btn-primary">Add</button>
                </div>
            </fieldset>
    </form>
    </div>)
}

export default ShipmentForm;