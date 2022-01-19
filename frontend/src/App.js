import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./Pages/Home";
import Warehouse from "./Pages/Warehouse";
import Shipments from "./Pages/Shipments";
import Sidebar from "./Components/Sidebar";
import "./App.css";

function App() {
  return (
    <Router>
      <div>
        <Sidebar />
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/warehouses">
            <Warehouse />
          </Route>
          <Route path="/shipments">
            <Shipments />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
