import React from "react";
import {Button, Link} from "@mui/material";
import PieChart from "./components/PieChart";
import {Route, Router, Routes} from "react-router-dom";
import ClientList from "./pages/ClientList";


function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Welcome to Material-UI</h1>
      <Button variant="contained" color="primary">
        Click Me
      </Button>
        <PieChart />
    <Router>
      <div style={{ padding: "20px" }}>
        <h1>Welcome to My App</h1>

        {/* Hyperlink to the Client List page */}
        <Link to="/client-list">Go to Client List</Link>

        {/* Routes */}
        <Routes>
          <Route path="/" element={<h2>Home Page</h2>} />
          <Route path="/client-list" element={<ClientList />} />
        </Routes>
      </div>
    </Router>
    </div>
  );
}

export default App;
