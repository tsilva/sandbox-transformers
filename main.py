from transformers import pipeline

# Sentiment analysis
classifier = pipeline("sentiment-analysis")
results = classifier(["I love this!", "This is terrible."])
for text, result in zip(["I love this!", "This is terrible."], results):
    print(f"{text} -> {result['label']} ({result['score']:.4f})")

# Text generation
generator = pipeline("text-generation", model="gpt2")
output = generator("The future of AI is", max_new_tokens=30, num_return_sequences=1)
print(f"\n{output[0]['generated_text']}")
