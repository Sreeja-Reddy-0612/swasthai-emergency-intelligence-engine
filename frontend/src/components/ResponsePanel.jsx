import AgentTrace from "./AgentTrace";

export default function ResponsePanel({ data }) {

  if (!data) return null;

  return (
    <div style={{ marginTop: "30px", textAlign: "left", maxWidth: "900px" }}>

      <h2 style={{ marginBottom: "20px" }}>
        Emergency Level: {data.triage}
      </h2>

      <h3>Instructions</h3>

      <ul style={{ lineHeight: "1.8", marginBottom: "25px" }}>
        {data.instructions.map((step, index) => (
          <li key={index}>{step}</li>
        ))}
      </ul>

      <h3>Sources</h3>

      <ul style={{ lineHeight: "1.8", marginBottom: "25px" }}>
        {data.sources.map((src, index) => (
          <li key={index}>{src}</li>
        ))}
      </ul>

      <h3>Confidence</h3>

      <p style={{ marginBottom: "25px" }}>
        {data.confidence}
      </p>

      <AgentTrace trace={data.agent_trace} />

    </div>
  );
}
