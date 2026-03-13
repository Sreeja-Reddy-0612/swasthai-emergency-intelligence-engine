from ai_engine.input_processing.context_extractor import extract_context
from ai_engine.triage.triage_engine import classify_emergency


def run_emergency_pipeline(message, age=None):

    agent_trace = []

    context = extract_context(message)
    agent_trace.append("Context Agent: extracted symptoms")

    triage = classify_emergency(context)
    agent_trace.append("Triage Agent: classified emergency level")

    instructions = []

    if triage == "CRITICAL":

        instructions = [
            "Check if the patient is breathing.",
            "Call an ambulance immediately.",
            "If not breathing, start CPR.",
            "Continue chest compressions until help arrives."
        ]

    elif triage == "EMERGENCY":

        instructions = [
            "Keep the patient calm.",
            "Avoid movement of the affected area.",
            "Seek medical help immediately."
        ]

    elif triage == "URGENT":

        instructions = [
            "Cool the burn with running water.",
            "Do not apply ice directly.",
            "Cover with clean cloth."
        ]

    else:

        instructions = [
            "Unable to determine emergency severity.",
            "Please contact a healthcare professional."
        ]

    return {
        "triage": triage,
        "instructions": instructions,
        "sources": [],
        "confidence": 0.60,
        "agent_trace": agent_trace
    }