import { useState } from "react";
import EmergencyInput from "./components/EmergencyInput";
import ResponsePanel from "./components/ResponsePanel";
import { analyzeEmergency } from "./services/api";

function App() {

  const [data, setData] = useState(null);

  const handleSubmit = async (message) => {

    const result = await analyzeEmergency(message);

    setData(result);
  };

  return (
    <div>

      <h1>SwasthAI Emergency Assistant</h1>

      <EmergencyInput onSubmit={handleSubmit} />

      <ResponsePanel data={data} />

    </div>
  );
}

export default App;