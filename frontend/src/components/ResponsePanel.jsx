import AgentTrace from "./AgentTrace";
import "../styles.css";

export default function ResponsePanel({ data }) {

  if (!data) return null;

  const cleanInstructions = data.instructions.filter(
    (line) =>
      !line.toLowerCase().includes("you are an emergency medical assistant") &&
      !line.toLowerCase().includes("generate clear step") &&
      !line.toLowerCase().includes("return only numbered")
  );

  return (
    <div className="card">

      <div className="emergency-level">
        Emergency Level: {data.triage}
      </div>

      <div className="section-title">
        User Situation
      </div>
      <p className="text">{data.situation}</p>

      <div className="section-title">
        Medical Knowledge Hints
      </div>
      <ul className="list">
        {data.hints?.map((hint, i) => (
          <li key={i}>{hint}</li>
        ))}
      </ul>

      <div className="section-title">
        Trusted Medical Evidence
      </div>
      <ul className="list">
        {data.evidence?.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>

      <div className="section-title">
        Final First Aid Instructions
      </div>
      <ul className="list">
        {cleanInstructions.map((step, i) => (
          <li key={i}>{step}</li>
        ))}
      </ul>

      <div className="section-title">
        Medical Sources
      </div>
      <ul className="list">
        {data.sources.map((src, i) => (
          <li key={i}>{src}</li>
        ))}
      </ul>

      <div className="section-title">
        AI Confidence
      </div>
      <div className="confidence">
        {data.confidence}
      </div>

      <AgentTrace trace={data.agent_trace} />

    </div>
  );
}
