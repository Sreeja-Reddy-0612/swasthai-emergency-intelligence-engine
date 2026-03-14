from transformers import pipeline

_generator = None


def load_llm():

    global _generator

    if _generator is None:

        _generator = pipeline(
            "text-generation",
            model="google/flan-t5-base",
            max_length=200
        )

    return _generator


def run_reasoning_agent(state):

    generator = load_llm()

    query = state["message"]

    graph = "\n".join(state.get("graph_hints", []))

    evidence = "\n".join(state["evidence"])

    prompt = f"""
You are an emergency medical assistant.

User Situation:
{query}

Medical Knowledge Hints:
{graph}

Trusted Medical Evidence:
{evidence}

Generate clear step-by-step first aid instructions.

Return only numbered instructions.
"""

    output = generator(prompt)[0]["generated_text"]

    steps = []

    for line in output.split("\n"):

        if line.strip():
            steps.append(line.strip())

    state["instructions"] = steps

    state["agent_trace"].append(
        "Reasoning Agent: generated medical guidance"
    )

    return state
