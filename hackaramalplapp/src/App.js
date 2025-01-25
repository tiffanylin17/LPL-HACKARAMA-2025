import React, { useState } from "react";
import "./style.css";

function App() {
  const [responseData, setResponseData] = useState(null); // State to hold the response
  const [loading, setLoading] = useState(false); // State for loading indicator

  const Label = () => {
  return (
    <div className="label">
      <p className="published-styles-are">
        Published styles are shared with everyone on the team—they can be used
        by all team members in any of their files. Changing these styles will
        update them everywhere they&#39;re used.
        <br />
        <br />
        Change these default colors to your team’s colors by selecting a color
        layer and clicking on&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; in the Design
        panel to the right.
      </p>
    </div>
  );
};
  const handleButtonClick = async () => {
    setLoading(true);
    try {
      const response = await fetch("https://mkl79fjs9e.execute-api.us-east-1.amazonaws.com/prod/notificationHandler?name=test123!", {
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
      <p>hello test 123</p>

  );
}



export default App;
