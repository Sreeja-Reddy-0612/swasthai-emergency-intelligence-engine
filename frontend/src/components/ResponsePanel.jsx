export default function ResponsePanel({ data }) {

  if (!data) return null;

  return (
    <div>

      <h2>Emergency Level: {data.triage}</h2>

      <h3>Instructions</h3>

      <ul>
        {data.instructions.map((step, index) => (
          <li key={index}>{step}</li>
        ))}
      </ul>

      <h3>Agent Processing</h3>

      <ul>
        {data.agent_trace.map((step, index) => (
          <li key={index}>{step}</li>
        ))}
      </ul>

      <p>Confidence: {data.confidence}</p>

    </div>
  );
}