import { BrowserRouter, Routes, Route } from "react-router-dom";

import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import Warehouse from "./Pages/Warehouse";
import Navbar from "./Components/Navbar";
import Inventory from "./Pages/Inventory";
import Shipment from "./Pages/Shipment";
import Home from "./Pages/Home";

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
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
