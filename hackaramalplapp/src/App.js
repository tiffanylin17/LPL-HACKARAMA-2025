import React from "react";
import { Button } from "@mui/material";
import PieChart from "./components/PieChart";
import NavigationBar from "./components/NavigationBar";


function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Welcome to Material-UI</h1>
      <Button variant="contained" color="primary">
        Click Me
      </Button>
        <NavigationBar />
        <PieChart />
    </div>
  );
}

export default App;
