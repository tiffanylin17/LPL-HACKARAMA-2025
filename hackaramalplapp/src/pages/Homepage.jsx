import React, { useEffect, useState } from "react";
import ClientGrid from "../components/ClientGrid";

const Homepage = () => {
  const [clients, setClients] = useState([]);

  // Fetch client data (replace with your API call or local data)
  useEffect(() => {
    const fetchClients = async () => {
      // Replace this with an actual API call to your Lambda function
      const response = await fetch(
        "https://705msz21we.execute-api.us-west-2.amazonaws.com/prod/query_clients_by_advisor?advisor_id=12345"
      );
      const data = await response.json();

      // Ensure each row has a unique `id` for MUI DataGrid
      const rows = data.clients.map((client, index) => ({
        ...client,
        id: index + 1, // Assign a unique ID if not provided
      }));

      setClients(rows);
    };

    fetchClients();
  }, []);

  return (
    <div>
      <h1>Advisor Clients</h1>
      <ClientGrid clients={clients} />
    </div>
  );
};

export default Homepage;
