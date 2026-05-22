import React, { useState } from "react";
import axios from "axios";

function Detect() {
  const [image, setImage] = useState(null);
  const [result, setResult] = useState("");

  const upload = async () => {
    const formData = new FormData();
    formData.append("image", image);

    const res = await axios.post("http://localhost:5000/detect", formData);
    setResult(res.data.result + " (" + res.data.severity + ")");
  };

  return (
    <div style={{ textAlign: "center" }}>
      <h1>AI Crack Detection</h1>
      <input type="file" onChange={(e) => setImage(e.target.files[0])} />
      <br /><br />
      <button onClick={upload}>Detect</button>
      <h2>{result}</h2>
    </div>
  );
}

export default Detect;