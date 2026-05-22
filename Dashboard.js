import React, { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/history")
      .then(res => setData(res.data));
  }, []);

  return (
    <div>
      <h1>History</h1>
      {data.map((item, index) => (
        <div key={index}>
          <p>{item.filename} - {item.result} - {item.severity}</p>
        </div>
      ))}
    </div>
  );
}

export default Dashboard;