from local_models.ollama_utils import ollama_generate


def main():
    prompt = """
You are an AI tutor.
Explain what FrozenLake environment is in Reinforcement Learning.
Also explain why Q-learning is suitable for this task.
"""

    answer = ollama_generate(prompt, model="llama3")

    print("Prompt:")
    print(prompt)
    print("\nResponse:")
    print(answer)


if __name__ == "__main__":
    main()
