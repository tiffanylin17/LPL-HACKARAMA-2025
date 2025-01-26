import React from "react";
import { Pie } from "react-chartjs-2";
import { Card, CardContent, Typography } from "@mui/material";

// Chart.js needs to be registered for usage
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from "chart.js";

// Register required Chart.js components
ChartJS.register(ArcElement, Tooltip, Legend);

const PieChart = () => {
  // Data for the pie chart
  const data = {
    labels: ["High", "Moderate", "Low"],
    datasets: [
      {
        label: "Clients",
        data: [2, 8, 190],
        backgroundColor: [
          "rgba(255, 0, 0, 0.6)",
          "rgba(255, 206, 86, 0.6)",
          "rgba(0, 255, 0, 0.6)"
        ],
        borderColor: [
          "rgba(255, 0, 0, 1)",
          "rgba(255, 206, 86, 1)",
          "rgba(0, 255, 0, 1)"
        ],
        borderWidth: 1,
        hoverOffset: 10 // Creates a hover effect
      }
    ]
  };

  // Chart options
  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top" // Positioning the legend
      },
      tooltip: {
        callbacks: {
          label: (tooltipItem) =>
            `${tooltipItem.label}: ${tooltipItem.raw}`
        }
      }
    }
  };

  return (
    <Card>
      <CardContent>
        <Typography variant="h5" gutterBottom>
          Client Retention Risk Chart
        </Typography>
        <div style={{ width: "500px", height: "500px", marginLeft: "0" }}>
          {/* Adjust chart size and align it to the left */}
          <Pie data={data} options={options} />
        </div>
      </CardContent>
    </Card>
  );
};

export default PieChart;
