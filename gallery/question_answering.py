from transformers import pipeline

qa = pipeline("question-answering")

context = """
Hugging Face is a company that develops tools for building applications using machine learning.
It is most notable for its Transformers library built for natural language processing applications
and its platform that allows users to share machine learning models and datasets. The company
was founded in 2016 and is headquartered in New York City.
"""

questions = [
    "What is Hugging Face?",
    "When was the company founded?",
    "Where is Hugging Face headquartered?",
]

for question in questions:
    result = qa(question=question, context=context)
    print(f"Q: {question}")
    print(f"A: {result['answer']} (score: {result['score']:.4f})\n")
