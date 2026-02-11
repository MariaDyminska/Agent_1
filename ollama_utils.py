import requests


def ollama_generate(prompt: str, model: str = "llama3") -> str:
  

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    return response.json()["response"]
