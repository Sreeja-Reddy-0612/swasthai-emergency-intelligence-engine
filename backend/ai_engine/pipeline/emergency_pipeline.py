from ai_engine.input_processing.context_extractor import extract_context
from ai_engine.triage.triage_engine import classify_emergency
from ai_engine.rag.retriever import retrieve


def run_emergency_pipeline(message, age=None):

    agent_trace = []

    context = extract_context(message)
    agent_trace.append("Context Agent: extracted symptoms")

    triage = classify_emergency(context)
    agent_trace.append("Triage Agent: classified emergency level")

    evidence = retrieve(message)

    agent_trace.append("Retrieval Agent: retrieved medical evidence")

    instructions = evidence

    return {
        "triage": triage,
        "instructions": instructions,
        "sources": ["WHO / Red Cross First Aid"],
        "confidence": 0.75,
        "agent_trace": agent_trace
    }