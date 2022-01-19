import React from 'react'

function WarehouseForm() {
    return (
        <div className="container">
            <form style={{
            width:"50%",
            marginTop:"2%",
            marginLeft:"10%",
        }}>
            <fieldset>
                <legend>Add a new Warehouse</legend>
            <div className="row">
                <div className="col-lg-6">
                    <div className="mb-3">
                        <label for="exampleInputEmail1" className="form-label">Name<sup>*</sup></label>
                        <input type="text" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder='Warehouse name' required/>
                </div>
                </div>
                <div className="col-lg-6">
                    <div className="mb-3">
                        <label for="exampleInputPassword1" className="form-label">Location<sup>*</sup></label>
                        <input type="text" className="form-control" id="exampleInputPassword1" placeholder='(i.e, 24th street, Nasr City, Cairo, Egypt)' required/>
                </div>
                </div>
            </div>
            <button type="submit" className="btn btn-primary">Add</button>
            </fieldset>
            </form>
        </div>
    )
}

export default WarehouseForm
