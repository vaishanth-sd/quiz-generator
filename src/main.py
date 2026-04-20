# src/main.py

import random
from utils import extract_answers, is_valid_question
from qg import generate_question
from distractor import generate_distractors_llm, clean_distractors


def generate_mcqs(text):
    answers = extract_answers(text)
    mcqs = []
    seen_questions = set()

    for ans in answers:
        try:
            question = generate_question(text, ans)

            if not is_valid_question(question, ans):
                continue

            if question in seen_questions:
                continue

            seen_questions.add(question)

            distractors = clean_distractors(
                generate_distractors_llm(question, ans)
            )

            options = distractors + [ans]
            options = list(dict.fromkeys(options))

            while len(options) < 4:
                options.append(random.choice(answers))

            options = options[:4]
            random.shuffle(options)

            mcqs.append({
                "question": question,
                "options": options,
                "answer": ans
            })

        except Exception as e:
            print("Error:", e)

    return mcqs


if __name__ == "__main__":
    text = """
    Artificial Intelligence is a branch of computer science.
    It was founded in 1956 at the Dartmouth Conference.
    """

    mcqs = generate_mcqs(text)

    for i, q in enumerate(mcqs, 1):
        print(f"Q{i}: {q['question']}")
        for opt in q['options']:
            print(f" - {opt}")
        print("Answer:", q['answer'])
        print("-" * 50)