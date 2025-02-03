from transformers import pipeline
import gradio as gr

pipe = pipeline("text-generation", model="openai-community/gpt2")

gr.Interface.from_pipeline(pipe).launch()