from transformers import pipeline

asr = pipeline("automatic-speech-recognition")

url = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"

result = asr(url)
print(result["text"])
