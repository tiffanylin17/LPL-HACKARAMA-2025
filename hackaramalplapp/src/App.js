import React from "react";
import { Button } from "@mui/material";
import PieChart from "./components/PieChart";


function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>LPL Financial Client Retention Dashboard</h1>
      <Button variant="contained" color="primary">
        Click Me
      </Button>
        <PieChart />
    </div>
  );
}

export default App;
