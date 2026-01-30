from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")

texts = [
    "Hello, how are you?",
    "The weather is beautiful today.",
    "I love programming with Python.",
]

for text in texts:
    result = translator(text)
    print(f"{text} -> {result[0]['translation_text']}")
