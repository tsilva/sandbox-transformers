from transformers import pipeline

ner = pipeline("token-classification", aggregation_strategy="simple")

text = "Hugging Face is based in New York City and was founded by Clément Delangue and Julien Chaumond."

results = ner(text)
for entity in results:
    print(f"{entity['word']:>25} | {entity['entity_group']:<10} | score: {entity['score']:.4f}")
