import { useState } from "react";
import ResponsePanel from "./components/ResponsePanel";

export default function App() {

  const [input, setInput] = useState("");
  const [data, setData] = useState(null);

  const analyze = async () => {

    const res = await fetch("http://127.0.0.1:8000/api/emergency/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: input
      })
    });

    const json = await res.json();

    setData(json);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>

      <h1>SwasthAI Emergency Assistant</h1>

      <textarea
        rows="3"
        cols="50"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <br /><br />

      <button onClick={analyze}>
        Analyze Emergency
      </button>

      <ResponsePanel data={data} />

    </div>
  );
}
