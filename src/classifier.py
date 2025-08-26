import json
from pathlib import Path
from transformers import pipeline

CATEGORIES_PATH = Path("input/categories.json")

CATEGORIES = []
with open(CATEGORIES_PATH, "r") as categories_file:
    CATEGORIES = json.load(categories_file)

model_name = "google/gemma-3-4b-it"

pipe = pipeline(
    "text-generation",
    model=model_name,
)


def classify_text(text: str, categories=CATEGORIES):
    prompt = f"""
    You will classify websites based on their content. Choose the most approproriate from the following categories: {', '.join(categories)}. Return the most appropriate category name and nothing more. Website content:
    {text}
    """

    messages = [{"role": "user", "content": prompt}]

    result = pipe(messages)

    return result[0]["generated_text"][1]["content"]
