# TODO: turn into isolate project
# TODO: target notebook through command line
# TODO: register as global app with shortcut
# TODO: tag modified cells with digest of code + prompt
# TODO: make sure the rewriting takes surrounding context into account
# TODO: use langchain to be able to use different models

import nbformat
import openai
import json
import os
import re
from dotenv import load_dotenv
from tqdm import tqdm

def rewrite_markdown_with_gpt(notebook_path, output_notebook_path, openai_api_key):
    """
    Opens a Jupyter Notebook, rewrites Markdown cells for conciseness using GPT-4o,
    and saves the modified notebook.  Uses tqdm for progress display.

    Args:
        notebook_path: Path to the input Jupyter Notebook (.ipynb).
        output_notebook_path: Path to save the modified Jupyter Notebook.
        openai_api_key: Your OpenAI API key.
    """

    # Load the notebook
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
    except FileNotFoundError:
        print(f"Error: Notebook file not found at {notebook_path}")
        return
    except Exception as e:
        print(f"Error reading notebook: {e}")
        return

    # Initialize OpenAI client (if API key is provided and valid)
    if openai_api_key:
        try:
            client = openai.OpenAI(api_key=openai_api_key)
        except Exception as e:
            print(f"Error initializing OpenAI client: {e}")
            return
    else:
        print("Error: OpenAI API key is required.")
        return

    # Get markdown cells
    markdown_cells = [cell for cell in nb.cells if cell.cell_type == 'markdown']
    num_markdown_cells = len(markdown_cells)

    # Iterate through markdown cells with tqdm progress bar
    with tqdm(total=num_markdown_cells, desc="Rewriting Markdown Cells") as pbar:
        for cell in markdown_cells:
            original_markdown = cell.source

            #  Clean up the markdown
            cleaned_markdown = _clean_markdown(original_markdown)
            if not cleaned_markdown.strip():  # Skip if empty
                pbar.update(1) # update progress even if skipped.
                continue

            try:
                # Use GPT-4o to rewrite
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant that rewrites markdown text to be more concise and clear, while preserving all of the original meaning and information.  Maintain markdown formatting.  Do not add any extra introductory or concluding phrases; just return the revised markdown."
                        },
                        {
                            "role": "user",
                            "content": cleaned_markdown
                        }
                    ],
                    temperature=0.2,
                    max_tokens=1024,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                rewritten_markdown = response.choices[0].message.content.strip()
                cell.source = rewritten_markdown

            except openai.APIConnectionError as e:
                print(f"OpenAI Connection Error: {e}")
                return
            except openai.RateLimitError as e:
                print(f"OpenAI Rate Limit Error: {e}")
                return
            except openai.APIStatusError as e:
                print(f"OpenAI API Status Error: {e.status_code} - {e.response}")
                return
            except Exception as e:
                print(f"An unexpected error occurred with the OpenAI API: {e}")
                return
            finally:
                pbar.update(1)  # Update progress bar after each cell



    # Save the modified notebook
    try:
        with open(output_notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"Rewritten notebook saved to {output_notebook_path}")
    except Exception as e:
        print(f"Error writing output notebook: {e}")



def _clean_markdown(markdown_text):
    """
    Cleans up common issues in Markdown (same as before).
    """
    cleaned_text = re.sub(r'\n\s*\n', '\n\n', markdown_text).strip()
    cleaned_text = re.sub(r'', '', cleaned_text, flags=re.DOTALL)
    cleaned_text = re.sub(r'^( *[-+*]) +', r'\1 ', cleaned_text, flags=re.MULTILINE)
    cleaned_text = re.sub(r'^(#+) *(.+)$', r'\1 \2', cleaned_text, flags=re.MULTILINE)
    return cleaned_text


if __name__ == "__main__":
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    input_file = "HF_NLP_Course.ipynb"
    output_file = "output.ipynb"

    rewrite_markdown_with_gpt(input_file, output_file, openai_api_key)