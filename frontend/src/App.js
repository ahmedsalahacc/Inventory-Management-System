import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Inventories from "./Pages/Inventories";
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
            <Warehouse />
          </Route>
          <Route path="/inventories">
            <Inventories />
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
