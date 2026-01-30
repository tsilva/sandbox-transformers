from transformers import pipeline

classifier = pipeline("image-classification")

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"

results = classifier(url, top_k=5)
for result in results:
    print(f"{result['label']:>30} (score: {result['score']:.4f})")
