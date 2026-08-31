from langchain_mistralai import ChatMistralAI


def get_llm(temperature: float = 0.3):
    return ChatMistralAI(
        model="mistral-small-latest",
        temperature=temperature,
    )