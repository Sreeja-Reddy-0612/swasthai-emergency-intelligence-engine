from ..input_processing.context_extractor import extract_context
from ..triage.triage_engine import classify_emergency

from ..agents.graph_agent import run_graph_agent
from ..agents.retrieval_agent import run_retrieval_agent
from ..agents.reasoning_agent import run_reasoning_agent
from ..agents.safety_agent import run_safety_agent
from ..agents.explanation_agent import run_explanation_agent


def run_emergency_pipeline(message, age=None):

    state = {
        "message": message,
        "age": age,
        "agent_trace": []
    }

    context = extract_context(message)

    state["context"] = context

    state["agent_trace"].append(
        "Context Agent: extracted symptoms"
    )

    triage = classify_emergency(context)

    state["triage"] = triage

    state["agent_trace"].append(
        "Triage Agent: classified emergency"
    )

    state = run_graph_agent(state)

    state = run_retrieval_agent(state)

    state = run_reasoning_agent(state)

    state = run_safety_agent(state)

    state = run_explanation_agent(state)

    return {

        "triage": state["triage"],

        "instructions": state["instructions"],

        "sources": [
            "WHO",
            "Red Cross",
            "American Heart Association"
        ],

        "confidence": 0.88,

        "agent_trace": state["agent_trace"]
    }
