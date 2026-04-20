# src/config.py

from openai import OpenAI
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import spacy

# 🔹 Load NLP
nlp = spacy.load("en_core_web_sm")

# 🔹 QG model
qg_pipeline = pipeline(
    "text2text-generation",
    model="valhalla/t5-base-qg-hl",
    tokenizer="valhalla/t5-base-qg-hl"
)

# 🔹 Embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# 🔹 Groq client
client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.groq.com/openai/v1"
)