def run_explanation_agent(state):

    formatted = []

    for i, step in enumerate(state["instructions"]):
        formatted.append(f"{i+1}. {step.strip()}")

    state["instructions"] = formatted

    state["agent_trace"].append(
        "Explanation Agent: formatted output"
    )

    return state
