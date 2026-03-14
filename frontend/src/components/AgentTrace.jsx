export default function AgentTrace({ trace }) {

  if (!trace) return null;

  return (
    <div style={{ marginTop: "30px" }}>

      <h3>Agent Processing</h3>

      <ul style={{ lineHeight: "1.8" }}>
        {trace.map((step, index) => (
          <li key={index}>{step}</li>
        ))}
      </ul>

    </div>
  );
}
