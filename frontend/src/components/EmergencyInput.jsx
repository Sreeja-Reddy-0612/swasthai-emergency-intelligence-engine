import { useState } from "react";

export default function EmergencyInput({ onSubmit }) {

  const [message, setMessage] = useState("");

  return (
    <div>

      <textarea
        placeholder="Describe the emergency..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={() => onSubmit(message)}>
        Analyze Emergency
      </button>

    </div>
  );
}