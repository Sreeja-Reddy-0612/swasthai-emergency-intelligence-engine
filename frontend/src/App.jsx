import EmergencyInput from "./components/EmergencyInput";
import ResponsePanel from "./components/ResponsePanel";
import "./styles.css";
import { useState } from "react";

export default function App() {

  const [data, setData] = useState(null);

  const handleSubmit = async (message) => {

    const res = await fetch("http://127.0.0.1:8000/api/emergency/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const result = await res.json();

    setData(result);
  };

  return (

    <div className="app-container">

      <div className="title">
        SwasthAI Emergency Assistant
      </div>

      <EmergencyInput onSubmit={handleSubmit} />

      <ResponsePanel data={data} />

    </div>

  );
}
