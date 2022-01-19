import React from 'react'

function InventoryForm() {
    return (
        <div className="container">
            <form style={{
            width:"50%",
            marginTop:"2%",
            marginLeft:"10%",
        }}>
            <fieldset>
                <legend>Add a new Inventory</legend>
            <div className="row">
                <div className="col-lg-6">
                    <div className="mb-3">
                        <label for="exampleInputEmail1" className="form-label">Name<sup>*</sup></label>
                        <input type="text" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder='Inventory name' required/>
                </div>
                </div>
                <div className="col-lg-6">
                    <div className="mb-3">
                        <label for="disabledTextInput" className="form-label">Category<sup>*</sup></label>
                            <select id="disabledSelect" className="form-select" required>
                                 <option>Category</option>
                                 <option>Electronics</option>
                                 <option>Video Games</option>
                                 <option>Fashion</option>
                                 <option>Fragile</option>
                            </select>
                    </div>
                </div>
            </div>
            <div className="row">
                <div className="col-lg-6 mb-3">
                     <label for="disabledTextInput" className="form-label">Description</label>
                    <textarea className="form-control"  name="" id="" cols="40" rows="5" placeholder='description'></textarea>
                </div>
                <div className="col-lg-6">
                     <label for="disabledTextInput" className="form-label">Warehouse<sup>*</sup></label>
                            <select id="disabledSelect" className="form-select" required>
                                 <option>Select Warehouse</option>
                            </select>
                </div>
            </div>
            <button type="submit" className="btn btn-primary">Add</button>
            </fieldset>
            </form>
        </div>
    )
}

export default InventoryForm
