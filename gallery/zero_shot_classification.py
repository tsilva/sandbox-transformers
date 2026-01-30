from transformers import pipeline

classifier = pipeline("zero-shot-classification")

texts = [
    "The stock market crashed today after the Federal Reserve raised interest rates.",
    "The new iPhone features a revolutionary camera system.",
    "The team scored a last-minute goal to win the championship.",
]

labels = ["politics", "technology", "sports", "finance"]

for text in texts:
    result = classifier(text, candidate_labels=labels)
    print(f"\n{text}")
    for label, score in zip(result["labels"], result["scores"]):
        print(f"  {label:<15} {score:.4f}")
