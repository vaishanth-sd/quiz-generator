# src/distractor.py

from config import client

def generate_distractors_llm(question, answer):
    prompt = f"""
    Question: {question}
    Correct Answer: {answer}

    Generate exactly 3 incorrect but plausible answers.
    Return only comma-separated values.
    """

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        text = response.choices[0].message.content.strip()
        text = text.replace("\n", ",")

        parts = [p.strip("- ").strip() for p in text.split(",")]

        return list(dict.fromkeys(
            [p for p in parts if p and p.lower() != answer.lower()]
        ))[:3]

    except Exception as e:
        print("LLM Error:", e)
        return []


def clean_distractors(distractors):
    cleaned = []

    for d in distractors:
        d = d.strip()

        if d.lower().startswith("the "):
            d = d[4:]

        d = d[:1].upper() + d[1:]

        if d not in cleaned:
            cleaned.append(d)

    return cleaned