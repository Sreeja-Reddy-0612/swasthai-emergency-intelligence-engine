UNSAFE_TERMS = [
    "cut the wound",
    "suck the venom",
    "apply ice directly"
]


def run_safety_agent(state):

    safe = []

    for step in state["instructions"]:

        unsafe = False

        for term in UNSAFE_TERMS:
            if term in step.lower():
                unsafe = True

        if not unsafe and step.strip() != "":
            safe.append(step)

    state["instructions"] = safe

    state["agent_trace"].append(
        "Safety Agent: verified instructions"
    )

    return state
