import { BrowserRouter, Routes, Route } from "react-router-dom";

import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import Warehouse from "./Pages/Warehouse";
import Navbar from "./Components/Navbar";
import Inventory from "./Pages/Inventory";
import Shipment from "./Pages/Shipment";
import Home from "./Pages/Home";
import EditWarehouse from "./Pages/EditWarehouse";
import EditInventory from "./Pages/EditInventory";

function App() {
  return (
    <div className="App">
      <Navbar />
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/warehouses" element={<Warehouse />} />
          <Route exact path="/inventories" element={<Inventory />} />
          <Route exact path="/shipments" element={<Shipment />} />
          <Route exact path="/edit/warehouse/:id" element={<EditWarehouse />} />
          <Route exact path="/edit/inventory/:id" element={<EditInventory />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
