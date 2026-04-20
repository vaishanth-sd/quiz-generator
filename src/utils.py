# src/utils.py

from config import nlp

def extract_answers(text):
    doc = nlp(text)
    return list(set(ent.text for ent in doc.ents))


def highlight_answer(context, answer):
    return context.replace(answer, f"<hl> {answer} <hl>", 1)


def is_valid_question(question, answer):
    if not question or len(question) < 10:
        return False

    if answer.lower() in question.lower():
        return False

    bad_phrases = ["what planet does", "along with"]
    return not any(p in question.lower() for p in bad_phrases)