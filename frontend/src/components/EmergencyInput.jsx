import { useState } from "react";
import "../styles.css";

export default function EmergencyInput({ onSubmit }) {

  const [message, setMessage] = useState("");

  return (

    <div className="card">

      <div className="section-title">
        Describe Emergency Situation
      </div>

      <textarea
        placeholder="Example: child fell and fractured arm"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={() => onSubmit(message)}>
        Analyze Emergency
      </button>

    </div>

  );
}
