def fact_recall(generated, facts):
    generated = generated.lower()
    score = 0

    for fact in facts:
        words = fact.lower().split()
        match_count = sum(1 for word in words if word in generated)

        if match_count >= len(words) // 2:
            score += 1

    return score / len(facts)


def tone_accuracy(generated, tone):
    text = generated.lower()

    if tone == "formal":
        return 1 if any(w in text for w in ["dear", "regards"]) else 0.5
    elif tone == "casual":
        return 1 if "hi" in text else 0.5
    elif tone == "urgent":
        return 1 if any(w in text for w in ["urgent", "asap"]) else 0.5
    elif tone == "empathetic":
        return 1 if any(w in text for w in ["sorry", "apologize"]) else 0.5

    return 0.5


def conciseness(text):
    wc = len(text.split())
    if wc < 120:
        return 1
    elif wc < 200:
        return 0.7
    return 0.4