def extract_context(message: str):

    message = message.lower()

    symptoms = []

    if "faint" in message or "unconscious" in message:
        symptoms.append("unconscious")

    if "breathing" in message:
        symptoms.append("breathing_issue")

    if "bleeding" in message:
        symptoms.append("bleeding")

    if "snake" in message:
        symptoms.append("snake_bite")

    if "burn" in message:
        symptoms.append("burn")

    return {
        "message": message,
        "symptoms": symptoms
    }