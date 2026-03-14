from ..graph.medical_graph import medical_graph


def run_graph_agent(state):

    query = state["message"].lower()

    hints = []

    for condition in medical_graph:

        if condition in query:

            hints.append(medical_graph[condition]["hint"])
            hints.extend(medical_graph[condition]["risks"])

            state["agent_trace"].append(
                f"Graph Agent: detected condition '{condition}'"
            )

    state["graph_hints"] = hints

    return state
