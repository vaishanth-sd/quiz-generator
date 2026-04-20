# src/qg.py

from config import qg_pipeline
from utils import highlight_answer

def generate_question(context, answer):
    highlighted = highlight_answer(context, answer)

    input_text = f"generate question: {highlighted}"

    output = qg_pipeline(
        input_text,
        max_length=64,
        num_beams=5,
        early_stopping=True
    )

    question = output[0]['generated_text']

    return question.replace("<hl>", "").replace("</s>", "").strip()