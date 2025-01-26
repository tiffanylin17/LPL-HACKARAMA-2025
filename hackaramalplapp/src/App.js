import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

import { Button } from "@mui/material";
import PieChart from "./components/PieChart";
import ClientList from "./pages/ClientList"; // Import the Client List page


function App() {
  return (
    <Router>
      <div style={{ padding: "20px" }}>
        <h1>Welcome to Elijah's App</h1>

        {/* Hyperlink to the Client List page */}
        <Link to="/client-list">Go to Client List</Link>

        {/* Routes */}
        <Routes>
          <Route path="/" element={<h2>Home Page</h2>} />
          <Route path="/client-list" element={<ClientList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
