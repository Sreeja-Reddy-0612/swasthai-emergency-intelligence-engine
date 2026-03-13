def classify_emergency(context):

    symptoms = context["symptoms"]

    if "breathing_issue" in symptoms or "unconscious" in symptoms:
        return "CRITICAL"

    if "bleeding" in symptoms or "snake_bite" in symptoms:
        return "EMERGENCY"

    if "burn" in symptoms:
        return "URGENT"

    return "UNKNOWN"