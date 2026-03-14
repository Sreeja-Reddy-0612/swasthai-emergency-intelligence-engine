import "../styles.css";

export default function AgentTrace({ trace }) {

  if (!trace) return null;

  return (

    <div style={{ marginTop: "25px" }}>

      <div className="section-title">
        Agent Processing
      </div>

      {trace.map((step, index) => (
        <div key={index} className="agent-step">
          {step}
        </div>
      ))}

    </div>

  );
}
