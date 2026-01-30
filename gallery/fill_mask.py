from transformers import pipeline

unmasker = pipeline("fill-mask")

sentences = [
    "The capital of France is <mask>.",
    "Python is a popular <mask> language.",
    "The <mask> is the largest planet in our solar system.",
]

for sentence in sentences:
    print(f"\n{sentence}")
    results = unmasker(sentence, top_k=3)
    for result in results:
        print(f"  {result['token_str']:>15} (score: {result['score']:.4f})")
