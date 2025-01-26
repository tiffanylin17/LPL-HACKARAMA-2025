import React from "react";
import { Button } from "@mui/material";
import PieChart from "./components/PieChart";
import ClientList from "./pages/ClientList"; // Import the Client List page


function App() {
  return (
    <div style={{ padding: "20px" }}>
       <Router>
      {/* Navbar for navigation */}
      <Navbar />

      {/* Page Routing */}
      <Routes>
        <Route path="/" element={<h1>Welcome to the App</h1>} />
        <Route path="/client-list" element={<ClientList />} />
      </Routes>
    </Router>
    </div>
  );
}

export default App;
