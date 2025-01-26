import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import Button from "@mui/material/Button";
import {PieChart} from "@mui/icons-material";
import NavigationBar from "./components/NavigationBar";
import ClientList from "./pages/ClientList";

function App() {
  return (
    <Router>
      <div style={{ padding: "20px" }}>
        <h1>Welcome to Material-UI</h1>
        <Button variant="contained" color="primary">
          Click Me
        </Button>
        <NavigationBar />
        <PieChart />
      </div>
      <Routes>
        <Route path="/" element={<h2>Home Page</h2>} />
        <Route path="/ClientList" element={<ClientList />} />
        {/* Add other routes as needed */}
      </Routes>
    </Router>
  );
}

export default App;
