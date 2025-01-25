import React, { useState } from "react";

function App() {
  const [responseData, setResponseData] = useState(null); // State to hold the response
  const [loading, setLoading] = useState(false); // State for loading indicator

  const handleButtonClick = async () => {
    setLoading(true);
    try {
      const response = await fetch("https://mkl79fjs9e.execute-api.us-east-1.amazonaws.com/prod/notificationHandler?name=testing!", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
        // body: JSON.stringify({ name: "test" }), // Add the payload if required
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json(); // Parse the JSON response
      setResponseData(data); // Save the response data to state
    } catch (error) {
      console.error("Error fetching data:", error);
      setResponseData({ error: error.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Test API Endpoint</h1>
      <button onClick={handleButtonClick} disabled={loading}>
        {loading ? "Loading..." : "Send Request"}
      </button>
      <div style={{ marginTop: "20px" }}>
        <h2>Response:</h2>
        <pre>{responseData ? JSON.stringify(responseData, null, 2) : "No response yet"}</pre>
      </div>
    </div>
  );
}

export default App;
