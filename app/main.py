from fastapi import FastAPI
from google import genai
from google.genai import types

app = FastAPI()

client = genai.Client()

@app.get("/chat")
def chat(q: str):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=q,
    )
    return {"response": response.text}


@app.get("/chat-think")
def chat_think(q: str):
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=q,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="low")
        ),
    )
    return {"response": response.text}