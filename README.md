# 🧠 AI Quiz Generator

An intelligent system that generates **Multiple Choice Questions (MCQs)** from raw text using a hybrid **NLP + Deep Learning + LLM pipeline**.

---

## 📌 Overview

This project transforms plain text into structured MCQs by combining:

- Named Entity Recognition (NER)
- Transformer-based Question Generation
- LLM-powered distractor generation

It is designed for use in:
- LMS platforms
- EdTech tools
- Automated quiz systems

---

## ⚙️ Pipeline Architecture

1. **Answer Extraction**
   - Uses `spaCy` to extract key entities from text

2. **Question Generation**
   - Uses T5 model: `valhalla/t5-base-qg-hl`
   - Generates context-aware questions

3. **Distractor Generation**
   - Uses LLM API (Groq/OpenAI-compatible)
   - Produces plausible incorrect options

4. **Filtering & Validation**
   - Removes duplicate / low-quality questions
   - Ensures meaningful MCQs

---

## 🧩 Tech Stack

- Python
- HuggingFace Transformers
- Sentence Transformers
- spaCy
- LLM API (Groq / OpenAI compatible)

---

## 📂 Project Structure

quiz-generator/
│
├── src/
│ ├── config.py # Model + pipeline setup
│ ├── utils.py # Answer extraction + validation
│ ├── qg.py # Question generation logic
│ ├── distractors.py # LLM-based distractor generation
│ └── main.py # Entry point
│
├── notebook/
│ └── Untitled15.ipynb # Experimentation (Colab)
│
├── requirements.txt
└── README.md


---

## 🚀 Features

- Generate MCQs from any paragraph
- LLM-powered realistic distractors
- Duplicate filtering
- Modular architecture (easy to extend)
- Works with small or large text

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/main.py


Q: Where was Artificial Intelligence founded?
- MIT
- Stanford
- Dartmouth Conference
- Harvard

Answer: Dartmouth Conference


🔮 Future Improvements
PDF / DOCX / PPT input support
Web interface (React + FastAPI)
Fine-tuned question generation model
Difficulty-level control

👨‍💻 Author

Vaishanth S




⭐ If you like this project

Give it a star ⭐ and contribute!


---

# 🚀 PART 2 — Use CodeRabbit smartly (THIS is how you use it)

You don’t “run” CodeRabbit manually like code.

👉 It works via **GitHub Pull Requests (PRs)**

---

## ✅ Step-by-step to use CodeRabbit

### 1️⃣ Create a new branch

```bash
git checkout -b improve-readme