import React from "react";
import { DataGrid } from "@mui/x-data-grid";

const ClientGrid = ({ clients }) => {
  const columns = [
    { field: "id", headerName: "ID", width: 100 },
    { field: "first_name", headerName: "First Name", width: 150 },
    { field: "last_name", headerName: "Last Name", width: 150 },
    { field: "email", headerName: "Email", width: 200 },
    { field: "advisor_id", headerName: "Advisor ID", width: 150 },
    { field: "age", headerName: "Age", width: 100 },
    { field: "location", headerName: "Location", width: 150 },
    { field: "client_tenure", headerName: "Client Tenure", width: 150 },
    { field: "interaction_freq", headerName: "Interaction Frequency", width: 200 },
    { field: "last_interaction_date", headerName: "Last Interaction", width: 150 },
    { field: "portfolio_value", headerName: "Portfolio Value", width: 150 },
    { field: "investment_growth", headerName: "Investment Growth", width: 150 },
    { field: "survey_results", headerName: "Survey Results", width: 150 },
    { field: "login_freq", headerName: "Login Frequency", width: 150 },
    { field: "time_spent_on_cw", headerName: "Time on CW", width: 150 },
    { field: "stay_leave", headerName: "Stay/Leave", width: 150 },
  ];

  return (
    <div style={{ height: 500, width: "100%" }}>
      <DataGrid
        rows={clients}
        columns={columns}
        pageSize={10}
        rowsPerPageOptions={[5, 10, 20]}
        checkboxSelection
        disableSelectionOnClick
      />
    </div>
  );
};

export default ClientGrid;
