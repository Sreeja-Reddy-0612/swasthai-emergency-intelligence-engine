from transformers import pipeline
from ..utils.prompts import MEDICAL_REASONING_PROMPT

_generator = None


def load_llm():
    global _generator

    if _generator is None:
        _generator = pipeline(
            "text-generation",
            model="google/flan-t5-base",
            max_length=256
        )

    return _generator


def run_reasoning_agent(state):

    generator = load_llm()

    query = state["message"]

    evidence = "\n".join(state["evidence"])

    prompt = MEDICAL_REASONING_PROMPT.format(
        query=query,
        evidence=evidence
    )

    output = generator(prompt)[0]["generated_text"]

    steps = output.split("\n")

    state["instructions"] = steps

    state["agent_trace"].append(
        "Reasoning Agent: generated guidance"
    )

    return state
